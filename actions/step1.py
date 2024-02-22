from .common import action, delete_file
import time
import ftplib
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
import xml.etree.ElementTree as ET 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .archive_article import Archived_article_attribute
from .providers import Provider_model
import datetime


# function based view to get the file and perform step related actions
def step_actions(input_file_name, output_file_name):
    print("finding the file.")
    time.sleep(1)
    print("file found, now entering step 1 .........")
    time.sleep(1)
    output_file_name = action(input_file_name, output_file_name)
    delete_file(input_file_name)
    print("......... step 1 is over .........")
    return output_file_name


@api_view(['GET'])
def start_step1(request):
    due_for_download = Provider_model.objects.filter(
        next_due_date=datetime.datetime.today()
        )
    
    if not due_for_download.count():
        return HttpResponse("No pending action found")

    for item in due_for_download:
        try:
            connect = ftplib.FTP(item.host_name, item.user_id, item.pass_code)
            filename = "test.txt"
            with open(filename, "wb") as file:
                x = connect.retrbinary(f"RETR {filename}", file.write)
                Archived_artical_attribute.objects.create(
                    provider = item.provider_address,
                    file_name = x,
                    processed_on = datetime.datetime.now(),
                    status = 'waiting',
                )

                item.last_accessed_at = datetime.datetime.now()
                item.last_status = 'waiting'
                item.frequency = datetime.datetime.now() + datetime.timedelta(item.frequency)
                item.save()
        except:
            Archived_artical_attribute.objects.create(
                provider = item.provider_address,
                processed_on = datetime.datetime.now(),
                status = 'failed',
            )

            item.last_accessed_at = datetime.datetime.now()
            item.last_status = 'failed'
            item.frequency = datetime.datetime.now() + datetime.timedelta(item.frequency)
            item.save()

        connect.quit()

    return HttpResponse("done")

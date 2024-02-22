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
from .archive_article import Archived_article_attribute
from .providers import Provider_meta_data_FTP, Provider_model
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

# this function will fetch article from the FTP
@api_view(['GET'])
def start_step1(request):
    # get all providers that are due to be accessed today
    due_for_download = Provider_meta_data_FTP.objects.filter(
        next_due_date=datetime.datetime.today()
        )
    
    # if none is due to be accessed abort the process
    if not due_for_download.count():
        return HttpResponse("No pending action found")

    # if providers are due to be accessed
    for item in due_for_download:
        try:
            connect = ftplib.FTP(item.server, item.account, item.password)
            article_library = os.listdir(item.site_path)
            for article in article_library:
                with open(article, "wb") as file:
                    if not (Archived_artical_attribute.objects.filter(file_name=article).exists()):
                        x = connect.retrbinary(f"RETR {article}", file.write)
                        Archived_artical_attribute.objects.create(
                            provider = item.provider_address,
                            file_name = x,
                            processed_on = datetime.datetime.now(),
                            status = 'waiting',
                        )

                item.last_pull_time = datetime.datetime.now()
                item.last_pull_status = 'waiting'
                item.next_due_date = datetime.datetime.now() + datetime.timedelta(item.provider__minimum_delivery_fq)
                item.save()
        except:
            Archived_artical_attribute.objects.create(
                provider = item.provider_address,
                processed_on = datetime.datetime.now(),
                status = 'failed',
            )

            item.last_pull_time = datetime.datetime.now()
            item.last_pull_status = 'failed'
            item.next_due_date = datetime.datetime.now() + datetime.timedelta(item.provider__minimum_delivery_fq)
            item.save()
        connect.quit()

    return HttpResponse("done")

from .common import action, delete_file
import time
import ftplib
from django.http import HttpResponse
import os
from rest_framework.decorators import api_view
from .archive_article import Archived_article_attribute
from .archive_article import Archived_article_attribute
from .providers import Provider_meta_data_FTP
import datetime
from django.core.files.base import ContentFile


# this function will fetch article from the FTP
@api_view(['GET'])
def start_step1(request):
    # get all providers that are due to be accessed today
    due_for_download = Provider_meta_data_FTP.objects.all()
    
    # if none is due to be accessed abort the process
    if not due_for_download.count():
        return HttpResponse("No pending action found")

    # if providers are due to be accessed
    for item in due_for_download:

        # try to connect to FTP, if error occures update the record
        try:
            connect = ftplib.FTP(item.server)
            connect.login(item.account, item.password)
        except Exception as e:
            item.last_pull_time = datetime.datetime.today()
            item.last_pull_status = 'failed'
            item.next_due_date = datetime.datetime.today() + datetime.timedelta(item.provider.minimum_delivery_fq)
            item.save()
            continue

        # read the destination location

        connect.cwd(item.site_path)
        article_library = connect.nlst()

        # if record found explore inside
        if article_library:
            for article in article_library:
                try:
                    # if record not downloaded in our record and the the file size is not zero than download and write to our database
                    if not (Archived_article_attribute.objects.filter(file_name_on_ftp=article).exists()):
                        # with open(article, 'wb') as file:
                        #     connect.retrbinary(f'RETR {article}', file.write)

                        with open(article, 'wb') as file:
                            connect.retrbinary(f'RETR {article}', file.write)

                        with open(article, 'rb') as file:
                            _file = file.read()
                            # file.seek(0)
                            # file_content = file.read()
                            # Save to Django model
                            file_type = os.path.splitext(article)[1]
                            x = Archived_article_attribute.objects.create(
                                file_name_on_ftp = article,
                                provider = item.provider.official_name,
                                processed_on = datetime.datetime.today(),
                                status = 'waiting',
                                file_size = ContentFile(article).size,
                                file_type = file_type
                            )
                            x.file_content.save(article, _file)
                except Exception as e:
                    pass

        item.last_pull_time = datetime.datetime.today()
        item.last_pull_status = 'waiting'
        item.next_due_date = datetime.datetime.today() + datetime.timedelta(item.provider.minimum_delivery_fq)
        item.save()

        connect.quit()
    return HttpResponse("done")

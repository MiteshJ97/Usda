from .common import action, delete_file
import time
import ftplib
from django.http import HttpResponse
import os
from rest_framework.decorators import api_view
from .archive_article import Archived_article_attribute
from .archive_article import Archived_article_attribute
from .providers import Provider_meta_data_FTP, Provider_meta_data_API
import datetime
from io import BytesIO




def download_file(ftp, filename, local_path):
    with open(os.path.join(local_path, filename), 'wb') as f:
        ftp.retrbinary('RETR ' + filename, f.write)

def download_folder(ftp, folder_name, local_path):
    os.makedirs(os.path.join(local_path, folder_name), exist_ok=True)
    ftp.cwd(folder_name)
    filenames = ftp.nlst()
    for filename in filenames:
        if '.' in filename:  # It's a file
            download_file(ftp, filename, os.path.join(local_path, folder_name))
        else:  # It's a subfolder
            download_folder(ftp, filename, os.path.join(local_path, folder_name))
    ftp.cwd('..')



# this function will fetch article from the FTP
@api_view(['GET'])
def download_from_ftp(request):
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

        # if record found explore inside.
        if article_library:
            # iterate through each file
            for article in article_library:
                try:
                    # check if the article is file or directory
                    if not (os.path.isdir(article)):
                        file_size = connect.size(article)
                        # if record not downloaded in our record and the the file size is not zero than download and write to our database
                        if not (Archived_article_attribute.objects.filter(file_name_on_ftp=article).exists()):
                            content = BytesIO()
                            connect.retrbinary(f'RETR {article}', content.write)
                            content.seek(0)
                            file_type = os.path.splitext(article)[1]
                            x = Archived_article_attribute.objects.create(
                                file_name_on_ftp = article,
                                provider = item.provider.official_name,
                                processed_on = datetime.datetime.today(),
                                status = 'waiting',
                                file_size = file_size,
                                file_type = file_type
                            )
                            x.file_content.save(article, content)
                    else:
                        connect.file
                except Exception as e:
                    pass

        # update the last status
        item.last_pull_time = datetime.datetime.today()
        item.last_pull_status = 'waiting'
        item.next_due_date = datetime.datetime.today() + datetime.timedelta(item.provider.minimum_delivery_fq)
        item.save()

        # quite the connection
        connect.quit()

    return HttpResponse("done")



@api_view(['GET'])
def download_from_api(request):
    # get all providers that are due to be accessed today
    due_for_download = Provider_meta_data_API.objects.all()
    
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
                    file_size = connect.size(article)
                    # if record not downloaded in our record and the the file size is not zero than download and write to our database
                    if not (Archived_article_attribute.objects.filter(file_name_on_ftp=article).exists()):
                        # with open(article, 'wb') as file:
                        #     connect.retrbinary(f'RETR {article}', file.write)
                        content = BytesIO()
                        connect.retrbinary(f'RETR {article}', content.write)
                        content.seek(0)
                        # ftp_file = FTPFile.objects.create(name=article, path=connect.pwd(), size=file_size)
                        # ftp_file.content.save(article, content)
                        file_type = os.path.splitext(article)[1]
                        x = Archived_article_attribute.objects.create(
                            file_name_on_ftp = article,
                            provider = item.provider.official_name,
                            processed_on = datetime.datetime.today(),
                            status = 'waiting',
                            file_size = file_size,
                            file_type = file_type
                        )
                        x.file_content.save(article, content)
                except Exception as e:
                    pass

        item.last_pull_time = datetime.datetime.today()
        item.last_pull_status = 'waiting'
        item.next_due_date = datetime.datetime.today() + datetime.timedelta(item.provider.minimum_delivery_fq)
        item.save()

        connect.quit()
    return HttpResponse("done")


import ftplib
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def connectWithFTP(request):
    # Connect FTP Server
    connect = ftplib.FTP(settings.HOSTNAME, settings.USERNAME, settings.PASSWORD)

    # force UTF-8 encoding
    connect.encoding = "utf-8"

    # Enter File Name with Extension
    filename = "test.txt"
    # connect.cwd('/home/admin')

    # Write file in binary mode
    with open(filename, "wb") as file:
        # Command for Downloading the file "RETR filename"
        connect.retrbinary(f"RETR {filename}", file.write)
        
    # Display the content of downloaded file
    file= open(filename, "r")
    
    # Close the Connection
    connect.quit()


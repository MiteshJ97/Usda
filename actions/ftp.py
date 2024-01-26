import ftplib
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
import os
import xml.etree.ElementTree as ET 
from rest_framework.response import Response
from rest_framework.decorators import api_view
import time


def connect_with_ftp(request):
    try:
        # Connect FTP Server
        connect = ftplib.FTP(settings.HOSTNAME, settings.USERNAME, settings.PASSWORD)

        # force UTF-8 encoding
        connect.encoding = "utf-8"

        # Enter File Name with Extension
        filename = "test.txt"
        # connect.cwd('/home/admin')

        # Write file in binary mode
        with open(filename, "wb") as file:
            # Command for Downloading the file
            connect.retrbinary(f"RETR {filename}", file.write)
            
        # Display the content of downloaded file
        file = open(filename, "r")
        
        # Close the Connection
        connect.quit()
        return Response("File pulled from FTP successfullt")
    
    except Exception as e:
        return Response(f'''Error occured while pulling the content from the FTP. Error : {e}''')
    


# This function is required to read the xml file
def readXML(filename):
    # reading xml file , file name is vignan.xml 
    tree = ET.parse(filename) 
    
    # in our xml file student is the root for all  
    # student data. 
    data2 = tree.findall('Article') 
    
    # retrieving the data and insert into table 
    # i value for xml data #j value printing number of  
    # values that are stored 
    for i, j in zip(data2, range(1, 6)): 
        publisherName = i.find('PublisherName').text 
        journalTitle = i.find('JournalTitle').text 
        issn = i.find('Issn').text 
        volume = i.find('Volume').text 
        issue = i.find('Issue').text 

        pubdate = tree.findall('PubDate')
        for k in zip(pubdate, range(1,9)):
            year = k.find('Year').text 
            month = k.find('Month').text
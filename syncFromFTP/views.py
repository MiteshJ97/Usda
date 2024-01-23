import ftplib
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
# import xml element tree 
import os
import xml.etree.ElementTree as ET 
from rest_framework.response import Response
from rest_framework.decorators import api_view
import time


def connectWithFTP():
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
        return True
    
    except Exception as e:
        return Response(e)
    


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
            
        


# Function to read the file
# This function will take file path as input and will return the file content    
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


# Function to save the file
# This function will take blob and file_name to save the blob with file_name
def save_blob_as_file(blob, output_file_path):
    with open(output_file_path, 'w') as output_file:
        output_file.write(blob)



# function to delete file by given path
def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error deleting file '{file_path}': {e}")


def action(inputfile, outputfile):
    time.sleep(2.5)
    # Replace 'input.txt' with the path to your text file
    input_file_path = inputfile 
    output_file_path = outputfile
    # Read the content of the file
    file_content = read_file(input_file_path)

    # Print the content (optional)
    print("Content of the file:")
    print(file_content)

    # Save the content as a new file
    save_blob_as_file(file_content, output_file_path)

    print(f"\nBlob saved as '{output_file_path}'.")

    time.sleep(2.5)
    return output_file_path




# function based view to get the file
@api_view(['GET'])
def dryRunSteps(request):
    print("############################### Executing step 1 #################################")
    outputFileName = action('test.txt', 'outputTest.txt')
    print("############################### step 1 is over #################################")

    print("############################### Executing step 2 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 2 is over #################################")

    print("############################### Executing step 3 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 3 is over #################################")

    print("############################### Executing step 4 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 4 is over #################################")

    print("############################### Executing step 5 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 5 is over #################################")

    print("############################### Executing step 6 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 6 is over #################################")

    print("############################### Executing step 7 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 7 is over #################################")

    print("############################### Executing step 8 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 8 is over #################################")

    print("############################### Executing step 9 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 9 is over #################################")

    print("############################### Executing step 10 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 10 is over #################################")

    print("############################### Executing step 11 #################################")
    outputFileName = action(outputFileName, 'outputTest.txt')
    print("############################### step 11 is over #################################")

    # delete input file
    delete_file(outputFileName)

    print("############################### exiting the process. Good Bye #################################")

    return Response("Successfully executed all 11 steps")
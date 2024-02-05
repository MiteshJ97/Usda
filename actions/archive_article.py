from django.db import models
from django.core.files.storage import FileSystemStorage
import os


# choices to be used for status of article attributs
CHOICES= (
    ('waiting', 'waiting'),
    ('processed','processed'),
    ('failed', 'failed')
)

# class to remove the exisiting file.
# This will be used when downloading same file again or another file with same name
class OverWriteStorage(FileSystemStorage):
    def get_replace_or_create_file(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(self.location, name))
            return super(OverWriteStorage, self).get_replace_or_create_file(name, max_length)


# Function to return the storage file path.
def get_file_path(instance, filename):
    return 'article_library_{0}/{1}'.format(instance.name, filename)


# Model to record logs of downloaded files/folders from FTP/SFTP's
class Archived_artical_attribute(models.Model):
    provider = models.URLField()
    file_name = models.FileField(upload_to=get_file_path, blank=True, null=True, storage=OverWriteStorage())
    location = models.TextField()
    received_on = models.DateTimeField(auto_now_add=True)
    processed_on = models.DateTimeField(null=True)
    status = models.CharField(max_lenght="10", choices=CHOICES)
    notes = models.TextField(defult="N/A")


    def __str__(self) -> str:
        return self.provider
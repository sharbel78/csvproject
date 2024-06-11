from django.db import models

# Create your models here.
class CSVfile(models.Model):
    file = models.FileField(upload_to='files/')
    uploaded=models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.

class Section_one(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    description_ar = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to='careers/',null=True,blank=True)
    def __str__(self):
        return self.title
   
   
class Reports(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/') 
    def __str__(self):
        return self.title
  
  

class Section_two(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    description_ar = models.TextField(null=True,blank=True)
    reports=models.ManyToManyField(Reports)
    def __str__(self):
        return self.title
    



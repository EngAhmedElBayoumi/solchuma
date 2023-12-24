from django.db import models
#import rich text field
from ckeditor.fields import RichTextField


# Create your models here.

#banner model image or video and title
class Banner(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    image_or_video = models.FileField(upload_to='banner/')
    def __str__(self):
        return self.title
    
#sipchem model icon , title , number , subtitle
class Sipchem(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    subtitle_ar = models.CharField(max_length=50)
    number = models.IntegerField()
    icon = models.FileField(upload_to='sipchem/')
    def __str__(self):
        return self.title
    
class Products(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField()
    description_ar = models.TextField()
    
    def __str__(self):
        return self.title

    
#investors title , description
class Investors(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return self.title
    
#sustainability title , description , icon nul=true
class Sustainability(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    description_ar = models.TextField(null=True,blank=True)
    icon = models.FileField(upload_to='sustainability/',null=True,blank=True)
    def __str__(self):
        return self.title
    
#careers title , description , image nul=true
class Careers(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField(null=True,blank=True)
    description_ar = models.TextField(null=True,blank=True)
    image = models.FileField(upload_to='careers/',null=True,blank=True)
    def __str__(self):
        return self.title
    



    
    

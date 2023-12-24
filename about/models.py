from django.db import models

# Create your models here.

#section 1
class section_one(models.Model):
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    description = models.TextField()
    description_ar = models.TextField()
    video_link = models.CharField(max_length=900)
    def __str__(self):
        return self.title
    
#section 2
class section_two(models.Model):
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
    image_ar = models.FileField(upload_to='images/')
    def __str__(self):
        return self.title
    
#section 3
class section_three(models.Model):
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return self.title
    
#section 4
class section_four(models.Model):
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    description = models.TextField()
    description_ar = models.TextField()
    icon = models.FileField(upload_to='images/')
    def __str__(self):
        return self.title

#section 5
class section_five(models.Model):
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    name_ar= models.CharField(max_length=200)
    description = models.TextField()
    description_ar = models.TextField()
    image = models.FileField(upload_to='images/')
    def __str__(self):
        return self.title
    
#Affiliates
class affiliates(models.Model):
    title= models.CharField(max_length=200)
    title_ar= models.CharField(max_length=200)
    main_image = models.FileField(upload_to='images/')
    description = models.TextField()
    description_ar = models.TextField()
    chart_image = models.FileField(upload_to='images/')
    Date = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    
#Investments
class investments(models.Model):
    title= models.CharField(max_length=200)
    title_ar= models.CharField(max_length=200)
    main_image = models.FileField(upload_to='images/')
    description = models.TextField()
    description_ar = models.TextField()
    chart_image = models.FileField(upload_to='images/')
    Date = models.CharField(max_length=200)
    def __str__(self):
        return self.title

#Board of Directors > name , image , job_profile
class board_of_directors(models.Model):
    name = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
    job_profile = models.CharField(max_length=200)
    job_profile_ar = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
#Executive Management > name , image , job_profile , description
class management_team(models.Model):
    name = models.CharField(max_length=200)
    name_ar = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')
    job_profile = models.CharField(max_length=200)
    job_profile_ar = models.CharField(max_length=200)
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return self.name
    

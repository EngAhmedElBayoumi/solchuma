from django.db import models
#import rich text field
from ckeditor.fields import RichTextField

# Create your models here.

#country code 
class Country_code(models.Model):
    country = models.CharField(max_length=200)
    country_ar = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    def __str__(self):
        return self.country
    
#messae type
class Message_type(models.Model):
    type = models.CharField(max_length=200)
    type_ar = models.CharField(max_length=200)
    def __str__(self):
        return self.type
    

#contact information model title , description , email , phone , address
class contact(models.Model):
    title = models.CharField(max_length=200)
    title_ar = models.CharField(max_length=200)
    description = models.TextField()
    description_ar = models.TextField()
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    address_ar = models.CharField(max_length=200)
    locaction = models.CharField(max_length=200)
    locaction_ar = models.CharField(max_length=200)
    aditional_info = models.RichTextField()
    aditional_info_ar = models.RichTextField()
    def __str__(self):
        return self.title
    
# contact message information name , email , phone , conuntry code , message type , subject , message
class contact_message(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    country_code = models.ForeignKey(Country_code, on_delete=models.CASCADE)
    message_type = models.ForeignKey(Message_type, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name
    

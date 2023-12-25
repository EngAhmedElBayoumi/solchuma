from django.db import models

class Product_specification(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title
    
class Safety_data(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title

class images(models.Model):
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.image.url
    
#sub category
class sub_category(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
class category(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    images = models.ManyToManyField(images, related_name='product_images',null=True,blank=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE)
    description = models.TextField()
    description_ar = models.TextField()
    product_specifications = models.ManyToManyField(Product_specification,null=True,blank=True)
    safety_data = models.ManyToManyField(Safety_data,null=True,blank=True)

    def __str__(self):
        return self.title

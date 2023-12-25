from django.db import models

# Create your models here.
#Digital Transformation

class Section_one(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    image=models.ImageField(upload_to='digital_transformation/section_one')
    def __str__(self):
        return self.title
    
class Section_two(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    def __str__(self):
        return self.title
class Section_three(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    image=models.ImageField(upload_to='digital_transformation/section_one')
    def __str__(self):
        return self.title


class Digital_transformation(models.Model):
    section_one=models.ForeignKey(Section_one,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    #many to many
    section_two=models.ManyToManyField(Section_two,null=True,blank=True)
    section_three=models.ForeignKey(Section_three,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    
#Research and Development

class Section_one_research(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    image=models.ImageField(upload_to='digital_transformation/section_one')
    def __str__(self):
        return self.title
    
class Section_two_research(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    def __str__(self):
        return self.title
class Section_three_research(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    image=models.ImageField(upload_to='digital_transformation/section_one')
    def __str__(self):
        return self.title

class Section_four_research(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    icon=models.FileField(upload_to='digital_transformation/section_one')
    def __str__(self):
        return self.title


class Research_and_development(models.Model):
    section_one=models.ForeignKey(Section_one_research,on_delete=models.CASCADE)
    section_two=models.ManyToManyField(Section_four_research,null=True,blank=True)
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100)
    description=models.TextField()
    description_ar=models.TextField()
    #many to many
    section_three=models.ManyToManyField(Section_two_research,null=True,blank=True)
    section_foure=models.ForeignKey(Section_three_research,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    


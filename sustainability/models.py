from django.db import models

# Create your models here.

#sustainability models

#Envronmental responsibility models

class Envronmental_section_one(models.Model):
    image = models.FileField(upload_to='images/')
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return self.description
    
class Envronmental_section_two(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return self.title
    
class Tab(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    description=models.TextField()
    description_ar=models.TextField()
    def __str__(self):
        return self.title
    
class Tabs(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    #many to many relationship
    tab = models.ManyToManyField(Tab)
    def __str__(self):
        return self.title    


    
class Envronmental(models.Model):
    section_one = models.ForeignKey(Envronmental_section_one, on_delete=models.CASCADE)
    section_two = models.ForeignKey(Envronmental_section_two, on_delete=models.CASCADE)
    tabs = models.ForeignKey(Tabs, on_delete=models.CASCADE)
    def __str__(self):
       # return f'environmental' + {self.id}'
        return f'environmental : ' + str(self.id)

    
#social responsibility models

class Social_section_one(models.Model):
    image = models.FileField(upload_to='images/')
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return self.title
    
class Social_section_two(models.Model):
    title = models.CharField(max_length=50)
    title_ar = models.CharField(max_length=50)
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return self.title

class Social(models.Model):
    section_one = models.ForeignKey(Social_section_one, on_delete=models.CASCADE)
    section_two = models.ForeignKey(Social_section_two, on_delete=models.CASCADE)
    def __str__(self):
        return f'social : ' + str(self.id)
    

# Governance responsibility models

#pdf
class files(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdf/')
    def __str__(self):
        return self.pdf.name


class Governance_section_one(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    description = models.TextField()
    description_ar = models.TextField()
    pdf=models.ManyToManyField(files)
    image=models.FileField(upload_to='images/')
    def __str__(self):
        return self.title
    
    
#crs models
class Crs_section_one(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    description = models.TextField()
    description_ar = models.TextField()
    url=models.URLField()
    def __str__(self):
        return self.title
    
class statistics(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    number=models.IntegerField()
    symbol=models.CharField(max_length=50)
    def __str__(self):
        return self.title
    
class Crs_section_two(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    statistics=models.ManyToManyField(statistics)
    def __str__(self):
        return self.title
    
class descriptions(models.Model):
    description = models.TextField()
    description_ar = models.TextField()
    def __str__(self):
        return f'description : ' + str(self.id)
    
class Crs_section_three(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    description=models.ManyToManyField(descriptions)
    def __str__(self):
        return self.title
    
class Crs_section_four(models.Model):
    title=models.CharField(max_length=50)
    title_ar=models.CharField(max_length=50)
    description=models.TextField()
    description_ar=models.TextField()
    image=models.FileField(upload_to='images/')
    def __str__(self):
        return self.title


#Sustainability Reports
class Sustainability_reports(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    def __str__(self):
        #year+title
        return self.year + ' ' + self.title
    #order
    class Meta:
        #order -year
        ordering = ['-year']
        
        
#IMS Reports
class Ims_reports(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    def __str__(self):
        #year+title
        return self.year + ' ' + self.title
    #order
    class Meta:
        #order -year
        ordering = ['-year']    
        
#Certifications
class Certifications(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')
    def __str__(self):
        #year+title
        return self.title 

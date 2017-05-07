from django.db import models

class DAGR(models.Model):
    def __str__(self):
        return self.Name
    Name = models.CharField("Name",max_length = 50)
    Author = models.CharField("Author",max_length = 50)
    CreationTime = models.DateTimeField("Creation Time")
    LastModified = models.DateTimeField("Last Modified", blank = True,null=True)
    DeletionTime = models.DateTimeField("Deletion Time", blank = True,null=True)
    HasKids = models.BooleanField("Has Kids", blank = True)

class Category(models.Model):
    Name = models.CharField("Name",max_length = 50)
    ParentCategory = models.ForeignKey("self",null = True,blank = True)
    DAGR =  models.ManyToManyField(DAGR,through = "DAGRCategory")


class Document(models.Model):
    Name = models.CharField("Name",max_length = 50, blank = True,null=True)
    Author = models.CharField("Author",max_length = 50)
    CreationTime = models.DateTimeField("Creation Time")
    LastModified = models.DateTimeField("Last Modified", blank = True,null=True)
    Size  = models.IntegerField("Size")
    Links = models.FileField(upload_to = 'files/')
    FileName = models.CharField("File Name",max_length = 50, unique = True)
    Type = models.CharField("Type",max_length = 50)
    Owner = models.ForeignKey(DAGR, blank = True,null=True)

class DAGRCategory(models.Model):
    CategoryID =  models.ForeignKey(Category)
    DAGRID = models.ForeignKey(DAGR)

class DAGRChildren(models.Model):
    Parent =  models.ForeignKey(DAGR,related_name='Parent')
    Children  =  models.ForeignKey(DAGR,related_name='Child')

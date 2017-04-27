from django.db import models

# Create your models here.

class DAGR(models.Model):
    Name = models.CharField("Name",max_length = 50)
    Author = models.CharField("Author",max_length = 50)
    CreationTime = models.DateTimeField("Creation Time")
    LastModified = models.DateTimeField("Last Modified")
    Size = models.CharField("Size",max_length = 50)
    DeletionTime = models.DateTimeField("Deletion Time")
    HasKids = models.BooleanField("Has Kids")

class Category(models.Model):
    Name = models.CharField("Name",max_length = 50)
    ParentCategory = models.ForeignKey("self")

class Document(models.Model):
    Name = models.CharField("Name",max_length = 50)
    Author = models.CharField("Author",max_length = 50)
    CreationTime = models.DateTimeField("Creation Time")
    LastModified = models.DateTimeField("Last Modified")
    Size  = models.IntegerField("Size")
    Links = models.FileField(upload_to = 'files/')
    Type = models.CharField("Type",max_length = 50)
    Owner = models.ForeignKey(DAGR)

class DAGRCategory(models.Model):
    Category =  models.ForeignKey(Category)
    DAGR =  models.ForeignKey(DAGR)


class DAGRChildren(models.Model):
    Parent =  models.ForeignKey(DAGR,related_name='Parent')
    Children  =  models.ForeignKey(DAGR,related_name='Child')

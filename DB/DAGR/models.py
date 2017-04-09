from django.db import models

# Create your models here.

class DAGR(models.Model):
    Name = models.CharField(_("Name"))
    Author = models.CharField(_("Author"))
    CreationTime = models.DateTimeField(_("Creation Time"))
    LastModified = models.DateTimeField(_("Last Modified"))
    Size = models.CharField(_("Size"))
    DeletionTime = models.DateTimeField(_("Deletion Time"))
    Has_Kids = models.BooleanField(("Has Kids"))

class Category(models.models):
    Name = models.CharField(_("Name"))
    ParentCategory = models.ForeignKey(_(Category))

class Document(models.Model):
    Name = models.CharField(_("Name"))
    Author = models.CharField(_("Author"))
    CreationTime = models.DateTimeField(_("Creation Time"))
    LastModified = models.DateTimeField(_("Last Modified"))
    Size  = models.IntegerField(_("Size"))
    Links = models.CharField(_("Link"))
    Type = models.CharField(_("Type"))
    Owner = models.ForeignKey(_(DAGR))

class DAGR_Category(models.Model):
    Category =  models.ForeignKey(_(Category))
    DAGR =  models.ForeignKey(_(DAGR))


class DAGR_Children(models.Model):
    Parent =  models.ForeignKey(_(DAGR))
    Children  =  models.ForeignKey(_(DAGR))

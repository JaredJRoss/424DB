from django.db import models

# Create your models here.

class DAGR(models.Model):
    Name = models.CharField(_("Name"))
    Author = models.CharField(_("Author"))
    CreationTime = models.DateTimeField(_("Creation Time"))
    LastModified = models.DateTimeField(_("Last Modified"))
    Size = models.CharField(_("Size"))
    DeletionTime = models.DateTimeField(_("Deletion Time"))
    Category =  models.CharField(_("Category"))


class Document(models.Model):
    Name = models.CharField(_("Name"))
    Links = models.CharField(_("Link"))
    Owner = models.ForeignKey(_(DAGR))


class DAGR_Children(models.Model):
    Parent =  models.ForeignKey(_(DAGR))
    Children  =  models.ForeignKey(_(DAGR))

from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.Name

    Name = models.CharField("Name",max_length = 50)
    ParentCategory = models.ForeignKey("self",null = True,blank = True)

class DAGR(models.Model):
    def get_absolute_url(self):
    	from django.urls import reverse
    	return reverse('dagr_detail', args=[str(self.id)])
    def __str__(self):
        return self.Name
    def __iter__(self):
        for field in self._meta.get_fields(include_parents = True):
            if field.name =='Kids':
                field.verbose_name = 'Kids'
                values = ''
                for kid in self.Kids.all():
                    values = values +'\n'+"\xa0\xa0\xa0\xa0"  + kid.__str__()
                yield(field,values)

            elif field.name == 'CategoryID':
                field.verbose_name = 'Category'
                values = ''
                for cat in self.CategoryID.all():
                    values = values +'\n'+"\xa0\xa0\xa0\xa0"  + cat.__str__()
                yield(field,values)
            else:
                value = getattr(self,field.name,None)
                yield(field,value)

    Name = models.CharField("Name",max_length = 50)
    Description = models.CharField("Description",max_length = 500,blank= True,null = True)
    Author = models.CharField("Author",max_length = 50)
    CreationTime = models.DateTimeField("Creation Time")
    LastModified = models.DateTimeField("Last Modified", blank = True,null=True)
    DeletionTime = models.DateTimeField("Deletion Time", blank = True,null=True)
    HasKids = models.BooleanField("Has Kids", blank = True)
    Kids = models.ManyToManyField("self",symmetrical=False,through = 'DAGRChildren',blank=True)
    CategoryID = models.ManyToManyField(Category,through = "DAGRCategory",blank = True)
    Size  = models.IntegerField("Size")

class Document(models.Model):
    def __str__(self):
        return self.Name

    Name = models.CharField("Name",max_length = 50, blank = True,null=True)
    Author = models.CharField("Author",max_length = 50)
    Size  = models.IntegerField("Size")
    Links = models.FileField(upload_to = 'files/')
    FileName = models.CharField("File Name",max_length = 50, unique = True)
    Type = models.CharField("Type",max_length = 50)
    Owner = models.ForeignKey(DAGR, blank = True,null=True)
    Description = models.CharField("Description",max_length = 100)


class URL(models.Model):
    def __str__(self):
        return self.Name

    Name = models.CharField("Name",max_length = 50, blank = True,null=True)
    Type = models.CharField("Type",max_length = 50)
    Description = models.CharField("Description",max_length = 100)
    Link = models.CharField("Link",max_length = 200)
    Owner = models.ForeignKey(DAGR, blank = True,null=True)

class DAGRCategory(models.Model):
    class Meta():
        auto_created=True

    CategoryID =  models.ForeignKey(Category)
    DAGRID = models.ForeignKey(DAGR)

class DAGRChildren(models.Model):
    class Meta():
        auto_created=True
    Parent =  models.ForeignKey(DAGR,related_name='Parent')
    Children  =  models.ForeignKey(DAGR,related_name='Child')

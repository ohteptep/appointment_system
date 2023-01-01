from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class depts(AbstractUser):
    admintype = [
        ('OAA','Office of Academic Affairs'),
        ('DIT','Department of Information Technology'),
        ('DLA','Department of Liberal Arts'),
        ('OCL','Office of Campus Library'),
        ('DED','Department of Education'),
        ('DMS','Department of Mathematics and Science'),
        ('DOE','Department of Engineering'),
        ('OSA','Office of Student Affairs'),
        ('UITC','University Information Technology Center'),
        ('DPE','Department of Physical Education'),
        ('SD','Security Department'),
        ('RE','Research & Extension'),
    ]
    positiontype = [
        ('Head','Head'),
        ('Faculty','Faculty'),
    ]

    department = models.CharField(max_length=200, choices = admintype, verbose_name = 'department')
    position = models.CharField(max_length=200, choices = positiontype, verbose_name = 'position')

class appointmentForm(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    yrlevel = models.CharField(max_length=100)
    yrgraduate = models.CharField(max_length=100)
    studentnum = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    contactperson = models.CharField(max_length=100)
    pdate = models.CharField(max_length=100)
    ptime = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    status = models.CharField(max_length=100) 
    notes = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    contactperson_email = models.CharField(max_length=100)
    date_submit = models.CharField(max_length=100)
    sd_status = models.CharField(max_length=100)

class cssform(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    transaction = models.CharField(max_length=100)
    signature = models.CharField(max_length=100)
    timeliness = models.IntegerField()
    completeness = models.IntegerField()
    professionalism = models.IntegerField()
    courteousness = models.IntegerField()
    overall = models.IntegerField()
    feedback = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)


class PDFS(models.Model):
    PDFSave = models.CharField(max_length=200, null=True)
import datetime
import json
import math

from django.db import models
from django.contrib.auth import  get_user_model
from rest_framework import status
from rest_framework.response import Response

User=get_user_model()
import _datetime
from django.utils.timezone import now
from django.utils import timezone
JOB_CATEGORIES=(
    ('IT - Software / Hardware / Networking','IT - Software / Hardware / Networking'),
    ('Business / Administration','Business / Administration'),
    ('Engineering','Engineering'),
    ('Marketing / Sales ','Marketing / Sales '),
    ('Medical / Healthcare','Medical / Healthcare'),
    ('Accounts / Finance','Accounts / Finance'),
    ('Education / Course / Language',"Education / Course / Language"),
    ('Other','Other')
)


PLACE=(
    ("Kathmandu","Kathmandu"),
    ("Pokhara","Pokhara"),
    ("Lalitpur","Lalitpur"),
    ("Bharatpur","Bharatpur"),
    ("Biratnagar","Biratnagar"),
    ("Janakpur","Janakpur"),
    ("Ghorahi","Ghorahi"),
    ("Hetauda","Hetauda"),
    ("Dhangadhi","Dhangadhi"),
    ("Tulsipur","Tulsipur"),
    ("Itahari","Itahari"),
    ("Nepalgunj","Nepalgunj"),
    ("Butwal","Butwal"),
    ("Dharan","Dharan"),
    ("Kalaiya","Kalaiya"),
    ("Jitpursimara","Jitpursimara"),
    ("Other","Other")

)


POSITION_TYPES=(
    ("Entry Level","Entry Level"),
    ("Intermediate","Intermediate"),
    ("Expert","Expert")

)

JOB_TYPES=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ("Contract","Contract")


)

# Create your models here.
class Jobs(models.Model):
    post_by=models.ForeignKey(User,on_delete=models.CASCADE,)
    company_name=models.CharField(max_length=255,blank=False,)
    location=models.CharField(max_length=255, choices=PLACE,)
    job_category=models.CharField(max_length=255, choices=JOB_CATEGORIES,blank=False,)
    position=models.CharField(max_length=255, blank=False,)
    experience=models.CharField(max_length=255,blank=False,)
    job_description=models.TextField(blank=False,)
    responsiblities=models.TextField(blank=False,)
    skill=models.TextField(blank=False,)
    education=models.CharField(max_length=255,blank=False,)
    what_we_offer=models.TextField(blank=True,)
    email=models.EmailField( blank=False,)
    post_date=models.DateField( default=_datetime.date.today, blank=False,editable=False)
    before_date=models.DateField(blank=False,)
    salary=models.CharField(max_length=255, blank=False,)
    position_type=models.CharField(max_length=255, choices=POSITION_TYPES,blank=False,)
    number_of_vacancy=models.CharField(max_length=255, blank=False,)
    job_type=models.CharField(max_length=255, choices=JOB_TYPES,blank=False,)
    days_left=models.IntegerField(null=True, blank=True)

    def save(self,*args, **kwargs):
        self.days_left=((self.before_date - self.post_date).days)
        if self.days_left>=0:
          super(Jobs, self).save(*args, **kwargs)
        else:
            return  False

    def delete_automaically(self):
        # time=self.post_date+datetime.timedelta(days=self.days_left)
        time=self.post_date
        if time<= 0:
            e=Jobs.objects.get(pk=self.pk)
            # Jobs.objects.get(pk=self.pk).delete()
            e.delete()
            return  True
        else:
            return False












class HitCount(models.Model):
    visits=models.IntegerField(default=0)




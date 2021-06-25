
from django.db import models


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

class CompanyRegistrationModel(models.Model):
    company_name=models.CharField(max_length=255,blank=False)
    email=models.EmailField(max_length=255,blank=False)
    contact_number=models.CharField(max_length=255, blank=True)
    password=models.CharField(max_length=255,blank=False)
    password1=models.CharField(max_length=255,blank=False)
    logo=models.ImageField(upload_to="logo/",blank=True)
    place=models.CharField(max_length=255,choices=PLACE,null=False,blank=False)








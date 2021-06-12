from django.db import models
from django.contrib.auth import  get_user_model
User=get_user_model()
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
    what_we_offer=models.TextField(blank=False,)
    email=models.EmailField( blank=False,)
    post_date=models.DateField( auto_now_add=True)
    before_date=models.DateField(blank=False,)

    # class Meta:
    #     ordering=['post_date']
    #
    # def __str__(self):
    #     return self.position




class HitCount(models.Model):
    visits=models.IntegerField(default=0)



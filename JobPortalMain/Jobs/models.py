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
    post_by=models.ForeignKey(User,on_delete=models.CASCADE,default='')
    location=models.CharField(max_length=255, choices=PLACE,default='')
    job_category=models.CharField(max_length=255, choices=JOB_CATEGORIES,blank=False,default='')
    position=models.CharField(max_length=255, blank=False,default='')
    experience=models.CharField(max_length=255,blank=False,default='')
    job_description=models.TextField(blank=False,default='')
    responsiblities=models.TextField(blank=False,default='')
    skill=models.TextField(blank=False,default='')
    education=models.CharField(max_length=255,blank=False,default='')
    what_we_offer=models.TextField(blank=False,default='')
    email=models.EmailField( blank=False,default='')
    post_date=models.DateField( auto_now_add=True)
    before_date=models.DateField(blank=False,default='2020-2-2')

    # class Meta:
    #     ordering=['post_date']
    #
    # def __str__(self):
    #     return self.position











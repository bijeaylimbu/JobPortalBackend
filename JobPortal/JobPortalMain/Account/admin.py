from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import  CompanyRegistrationModel

class CompanyRegisterAdmin(admin.ModelAdmin):
    list_display = ('company_name','email','contact_number','place')

admin.site.register(CompanyRegistrationModel,CompanyRegisterAdmin)

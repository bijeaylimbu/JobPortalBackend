from rest_framework import serializers
from .models import  Jobs,HitCount
class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields="__all__"

class HitCountSerializer(serializers.ModelSerializer):
    class Meta:
        model=HitCount
        fields="__all__"



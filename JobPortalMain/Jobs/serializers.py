from collections import OrderedDict
from operator import itemgetter

from rest_framework import serializers
from .models import  Jobs,HitCount
class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields="__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Here we filter the null values and creates a new dictionary
        # We use OrderedDict like in original method
        ret = OrderedDict(filter(itemgetter(1), ret.items()))
        return ret




class HitCountSerializer(serializers.ModelSerializer):
    class Meta:
        model=HitCount
        fields="__all__"



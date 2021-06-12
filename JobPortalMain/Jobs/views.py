import self as self
from django.shortcuts import render

# Create your views here.
from functools import reduce
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import django_filters
from .models import Jobs
from .serializers import JobsSerializer




class JobsView(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()


    permission_classes = (AllowAny,)
    serializer_class = JobsSerializer

    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['$position','$job_category']
    filterset_fields = ['job_category','location']


    # def get(self, request, format=None):
    #     users = Jobs.objects.all()
    #     serializer = JobsSerializer(users, many=True)
    #     return Response(serializer.data)


class JobDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()






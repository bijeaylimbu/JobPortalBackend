from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Jobs
from .serializers import JobsSerializer

class JobsView(generics.CreateAPIView):
    queryset = Jobs.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = JobsSerializer

    def get(self, request, format=None):
        users = Jobs.objects.all()
        serializer = JobsSerializer(users, many=True)
        return Response(serializer.data)

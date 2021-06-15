import datetime

from django.db.models import Q, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets

from rest_framework.generics import  RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Jobs,HitCount
from .serializers import JobsSerializer,HitCountSerializer
from django.http import HttpResponse



class JobsView(generics.ListCreateAPIView):
    queryset = Jobs.objects.all().select_related('post_by')
    permission_classes = (AllowAny,)
    serializer_class = JobsSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['$position','$job_category']
    filterset_fields = ['job_category','location']

    # def perform_create(self, serializer):
    #     start_date=datetime.datetime.strptime(self.request.data.get('before_date'),"%Y-%m-%d")
    #     end_date=datetime.datetime.strptime(self.request.data.get('post_date'),"%Y-%m-%d")
    #     diff=abs((end_date-start_date).days)
    #     print(diff)












class JobDetailView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = JobsSerializer
    queryset = Jobs.objects.all()





class RelatedJobsList(RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = JobsSerializer
    # queryset = Jobs.objects.all()

    def get_object(self):
        return Jobs.objects.filter(job_category=self.kwargs['job_category'])


class HitCountViewSet(viewsets.ModelViewSet):
    queryset = HitCount.objects.all()
    serializer_class =HitCountSerializer

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        HitCount.objects.filter(pk=instance.id).update(visits=F('visits')+1)
        serializer=self.get_serializer(instance)
        return Response(serializer.data)


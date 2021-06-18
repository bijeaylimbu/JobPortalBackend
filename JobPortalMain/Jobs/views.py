import datetime

from django.db.models import Q, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, viewsets, status
from rest_framework.decorators import action

from rest_framework.generics import  RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

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



    @action(methods=['delete'], detail=False)
    def detete(self,request,pk, format=None):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def get_queryset(self):
    #     if self.request.query_params:
    #         return  Jobs.objects.all()
    #     else:
    #         return Jobs.objects.none()

class JobDelete(generics.ListAPIView):
    queryset = Jobs.objects.all().select_related('post_by')
    permission_classes = (AllowAny,)
    serializer_class = JobsSerializer

    def delete(self,request,pk,format=None):
        snippet=self.get_object()
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def delete_post(self,pk,request):
    #     days_left=request.data.get('days_left')
    #     id=request.data.get('Jobs')
    #     post_instance=Jobs.objects.get(id=id)
    #     print("needed to delete")
    #     if days_left==0 and days_left==None:
    #
    #         post_instance.delete()
    #
    #         return Response(status=status.HTTP_200_OK)
    #     return Response(status=status.HTTP_304_NOT_MODIFIED)








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


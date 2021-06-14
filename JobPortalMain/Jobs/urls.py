from django.urls import path
from .views import JobsView,JobDetailView,HitCountViewSet,RelatedJobsList
urlpatterns=[

    # path('login/user',UserCreate().as_view()),
    path('all_jobs/<int:pk>/', JobDetailView.as_view()),
 path('all_jobs/', JobsView.as_view()),
    path('hitcount/', HitCountViewSet.as_view({'get': 'list'})),
     path('related_jobs/<job_category>/', RelatedJobsList.as_view()),


]

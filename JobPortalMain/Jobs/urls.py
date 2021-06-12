from django.urls import path
from .views import JobsView,JobDetailView,HitCountViewSet
urlpatterns=[

    # path('login/user',UserCreate().as_view()),
    path('all_jobs/<int:pk>/', JobDetailView.as_view()),
 path('all_jobs/', JobsView.as_view()),
    path('hitcount/', HitCountViewSet.as_view({'get': 'list'}))


]

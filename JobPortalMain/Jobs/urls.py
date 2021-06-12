from django.urls import path
from .views import JobsView,JobDetailView
urlpatterns=[

    # path('login/user',UserCreate().as_view()),
    path('all_jobs/<int:pk>/', JobDetailView.as_view()),
 path('all_jobs/', JobsView.as_view())


]

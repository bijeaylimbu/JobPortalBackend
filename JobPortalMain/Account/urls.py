from django.urls import path


from .views import  UserCreate,UserRegisterView,CompanyRegisterView

urlpatterns=[

    # path('login/user',UserCreate().as_view()),
    path('user_register/', UserRegisterView.as_view()),
path('company_register/', CompanyRegisterView.as_view()),

]
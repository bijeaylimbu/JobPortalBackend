from django.urls import path


from .views import  UserCreate,UserRegisterView,CompanyRegisterView,CompnayLoginView

urlpatterns=[

    # path('login/user',UserCreate().as_view()),
    path('user_register/', UserRegisterView.as_view()),
path('company_register/', CompanyRegisterView.as_view()),
    path('company_login',CompnayLoginView.as_view())
]
from django.urls import path

from .views import *
app_name = 'main'
urlpatterns = [
    path('register/', RegisterUserApiView.as_view(), name='register_user'),
    path('user_list/', StudentsApiView.as_view(), name='user_list'),
]
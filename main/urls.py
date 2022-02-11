from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (RegisterGroupApiView, RegisterUserApiView, StudentsApiView,
                    StudentsViewSet)

router = DefaultRouter()

router.register('user_list', StudentsViewSet)

app_name = 'main'
urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls',)),
    path('register/', RegisterUserApiView.as_view(), name='register_user'),
    path('user_list/', StudentsApiView.as_view(), name='user_list'),
    path('create_group/', RegisterGroupApiView.as_view(), name='create_group'),

]
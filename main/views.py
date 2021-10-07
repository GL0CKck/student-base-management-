from django.shortcuts import render

from .models import *

from .serializers import RegisterStudentSerializer, StudentsSerializer

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegisterUserApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterStudentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentsApiView(ListAPIView):
    queryset = Student.object.all()
    serializer_class = StudentsSerializer

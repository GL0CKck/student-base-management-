from django.shortcuts import render

from .models import Student, Group

from .serializers import RegisterStudentSerializer, StudentsSerializer, RegisterSubGroupSerializer

from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions


class RegisterUserApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterStudentSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class RegisterGroupApiView(APIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = RegisterSubGroupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)


class StudentsApiView(ListAPIView):
    queryset = Student.object.all()
    serializer_class = StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.object.all()
    serializer_class = StudentsSerializer
    permission_classes = [permissions.IsAuthenticated]


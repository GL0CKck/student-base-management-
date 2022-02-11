from rest_framework import permissions, status, viewsets, generics
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student, Group
from .serializers import (RegisterStudentSerializer,
                          RegisterSubGroupSerializer, StudentsSerializer, GroupSerializer)


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


class StudentsApiView(generics.ListAPIView):
    queryset = Student.object.all().select_related('group')
    serializer_class = StudentsSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.object.all().select_related('group')
    serializer_class = StudentsSerializer
    permission_classes = [permissions.IsAuthenticated]


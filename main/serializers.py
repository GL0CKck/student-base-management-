from rest_framework import serializers

from .models import *


class RegisterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'group', 'password')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGroup
        fields = ('name',)


class StudentsSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'group')



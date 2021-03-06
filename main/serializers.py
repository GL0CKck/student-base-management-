from rest_framework import serializers

from .models import Group, Student, SubGroup


class RegisterStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'group', 'password')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubGroup
        fields = ('name', 'is_headman')


class StudentsSerializer(serializers.ModelSerializer):

    group = GroupSerializer()

    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'group')


class RegisterSubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name', 'is_headman', 'super_group')
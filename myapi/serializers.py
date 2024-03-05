from rest_framework import serializers
from .models import Student

# myapi/serializers.py

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('fName', 'lName', 'id', 'grade', 'startDate')
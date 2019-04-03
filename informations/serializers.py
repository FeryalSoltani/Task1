from rest_framework import serializers
from . import models

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'firstName', 'lastName', 'UserID', 'PhoneNum', 'Email', 'DateTime', 'Address',)
        model = models.Data

from rest_framework import serializers
from .models import Lease



class LeaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lease
        fields = '__all__'
        
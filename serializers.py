from rest_framework import serializers
from .models import employee
#it serializes which ever class you want

#It is going to convert the data into JSON format
class employeeserializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields =('firstname','lastname')

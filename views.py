from django.shortcuts import render
#used to get HTTP response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employee
from . serializers import employeeserializer

class employeeList(APIView):

#display all the employees in the database
    def get(self,request):
        emp1= employee.objects.all()
        #this converts the object into JSON
        serializer= employeeserializer(emp1, many= True)
        return Response(serializer.data)
        

#helps to create a new data
    def post(self):
        pass


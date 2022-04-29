from django.contrib import admin
from .models import employee

#django admin is automatically created
#register gives the permission to update,delete etc the model's data 
admin.site.register(employee)


# Register your models here.

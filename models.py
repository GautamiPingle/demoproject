from django.db import models

class employee(models.Model):
    firstname= models.CharField(max_length= 10)
    lastname= models.CharField(max_length= 12)
    emp_ID=models.IntegerField()
    #method which returns the string
    def _str_(self):
        return self.firstname
import os.path
import uuid
from django.db import models

def unique_img_name(instance,filename):
    name = uuid.uuid4()
    extension = filename.split(".")[-1]
    generated_name = f"{name}.{extension}"
    return os.path.join("employees",generated_name)

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=40)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(unique=True)
    salary = models.DecimalField(decimal_places=2,max_digits=8)
    disabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    profile_pic = models.ImageField(upload_to=unique_img_name,default="employees/default.jpg")
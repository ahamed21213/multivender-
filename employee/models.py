from django.db import models

# Create your models here.
class employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    photo_name=models.ImageField(upload_to='image')
    phone_number=models.CharField(max_length=12,blank=True)
    email_name=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name
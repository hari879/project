from django.db import models

# Create your models here.
class login_Details(models.Model):
    
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    objects=models.Manager()
    class Meta:
        db_tabel:"calc_login_detail"

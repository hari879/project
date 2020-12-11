from django.db import models

# Create your models here.
class student(models.Model):

    userid = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    student_name = models.CharField(max_length=255)
    student_id = models.IntegerField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.IntegerField (max_length=20)
    Address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    tenth = models.CharField(max_length=255)
    twelve = models.CharField(max_length=255) 
    cgpa = models.CharField(max_length=255)
    no_backlog = models.IntegerField(max_length=10)
    c_backlog = models.IntegerField(max_length=10)  
    class Meta:
        db_tabel:"data_Stu_student"
    def __str__(self):
        return self.student_name +' '+self.student_id +' '+self.userid +' '+ self.password +' ' + self.email +' '+ self.phone + ' ' + self.Address +' ' + self.country +' ' + self.twelve +' ' + self.tenth +' ' + self.no_backlog +' ' + self.c_backlog +' ' + self.cgpa

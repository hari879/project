from django.db import models

# Create your models here.
class StudentDetails:
    email: str
    password: str
    StudentName: str
    studentId: int
    mobileno: int
    adress: str
    country: str
    SSC_cgpa: float
    inter_marks: int
    UG_Current_cgpa: float
    total_backlogs: int
    active_backlogs: int
    projects: str
    skills: str

class student1(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Material(models.Model):
    FileName=models.CharField(max_length=100)
    pdf=models.FileField(upload_to='materials/pdfs/')

    def __str__(self):
        return self.FileName

class student(models.Model):
    student_name = models.CharField(max_length=255)
    student_id = models.IntegerField()
    email = models.CharField(max_length=255)
    phone = models.IntegerField()
    Address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    tenth = models.CharField(max_length=255)
    twelve = models.CharField(max_length=255) 
    cgpa = models.CharField(max_length=255)
    no_backlog = models.IntegerField()
    c_backlog = models.IntegerField()  
    
    def str(self):
        return self.objects.all()

class Company(models.Model):
    Company_name = models.CharField(max_length=255)
    About_company = models.TextField()
    Company_link = models.URLField(max_length=255)
    Jobrole = models.CharField(max_length=255)
    Job_responsilities = models.TextField()
    Job_Salary = models.FloatField(max_length=5)
    Eligibility_cgpa = models.FloatField(max_length=5)
    Eligibility_branches = models.TextField()
    Eligible_Passedout_Batchs = models.CharField(max_length=255)
    Eligibility_education_gap = models.IntegerField()
    application_start_date =models.DateField(null=True)
    application_end_date = models.DateField(null=True)
    
    def str(self):
        return self.objects.all()




        


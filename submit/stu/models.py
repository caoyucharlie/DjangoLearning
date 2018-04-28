from django.db import models

# Create your models here.


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'sub_student'


class StudentInfo(models.Model):

    i_addr = models.CharField(max_length=30)
    s = models.OneToOneField(Student)

    class Meta:
        db_table = 'sub_Student_Info'

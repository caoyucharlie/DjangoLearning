from django.db import models

# Create your models here.


class Student(models.Model):

    s_name = models.CharField(max_length=10, null=True)
    s_tel = models.CharField(max_length=11, null=True)

    class Meta:
        db_table = 'sub_student'


class StudentInfo(models.Model):

    i_addr = models.CharField(max_length=30, null=True)
    i_image = models.ImageField(upload_to='upload', null=True)
    s = models.OneToOneField(Student)

    class Meta:
        db_table = 'sub_Student_Info'


class Visit(models.Model):
    v_url = models.CharField(max_length=30)
    v_tiems = models.IntegerField()

    class Meta:
        db_table = 'visit'

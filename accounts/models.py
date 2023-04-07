from django.db import models
from django.contrib.auth.models import AbstractUser
from exam.models import CourseModel

# Create your models here.


class UserAccounts(AbstractUser):
    is_student = models.BooleanField(default=False, null=False)
    is_counsellor = models.BooleanField(default=False, null=False)
    is_agent = models.BooleanField(default=False, null=False)
    first_name = None
    last_name = None

    def get_role(self):
        if self.is_student:
            return "student"
        elif self.is_counsellor:
            return "counsellor"
        elif self.is_agent:
            return "agent"
        else:
            return "admin"

    def get_deatiled_instance(self):
        if self.is_student:
            return StudentDetail.objects.get(user=self)
        elif self.is_counsellor:
            return CounsellorDetail.objects.get(user=self)
        elif self.is_agent:
            return AgencyDetail.objects.get(user=self)


class StudentDetail(models.Model):
    user = models.OneToOneField(UserAccounts, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    dob = models.DateField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class CounsellorDetail(models.Model):
    user = models.OneToOneField(UserAccounts, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


class AgencyDetail(models.Model):
    user = models.OneToOneField(UserAccounts, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    courses = models.ManyToManyField(CourseModel)

    def __str__(self):
        return self.user.username

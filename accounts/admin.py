from django.contrib import admin
from .models import UserAccounts, StudentDetail, CounsellorDetail, AgencyDetail

# Register your models here.

admin.site.register(UserAccounts)
admin.site.register(StudentDetail)
admin.site.register(CounsellorDetail)
admin.site.register(AgencyDetail)
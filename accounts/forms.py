from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserAccounts, StudentDetail, CounsellorDetail, AgencyDetail
from exam.models import CourseModel

class RegForm(UserCreationForm):
    class Meta:
        model = UserAccounts
        fields = ("username", "email")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None


class StudentRegForm(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields = "__all__"
        exclude = ("user",)
        widgets = {"dob": forms.DateInput(attrs={"type": "date"})}
        labels = {"dob": "Date of Birth"}


class CounsellorRegForm(forms.ModelForm):
    class Meta:
        model = CounsellorDetail
        fields = "__all__"
        exclude = ("user",)


# class AgencyRegForm(forms.ModelForm):

#     class Meta:
#         model = AgencyDetail
#         fields = "__all__"
#         exclude = ("user",)
#         labels = {"description": "Description (optional)", "courses": 'Pick Providing Courses(can edit later)' }

class AgencyRegForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=CourseModel.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Pick Providing Courses(can edit later)'
    )

    class Meta:
        model = AgencyDetail
        fields = "__all__"
        exclude = ("user",)
        labels = {"description": "Description (optional)"}



        


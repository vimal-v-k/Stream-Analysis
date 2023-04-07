from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView
from django.db import transaction
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .models import UserAccounts
from .forms import RegForm, StudentRegForm, CounsellorRegForm, AgencyRegForm
from counsellor_agent.models import CounsellorNotification, AgentNotification, StudentNotification

# Create your views here.


@login_required
def home_view(request):
    if request.user.is_student:
        return redirect("accounts:student_home")
    elif request.user.is_counsellor:
        return redirect("accounts:counsellor_home")
    elif request.user.is_agent:
        return redirect("accounts:agency_home")
    else:
        return redirect("/admin/")


@login_required
@user_passes_test(lambda u: u.is_student)
def student_home_view(request):
    notifications = StudentNotification.objects.filter(student=request.user)
    return render(request, "accounts/student_home.html", {"notifications": notifications})


@login_required
@user_passes_test(lambda u: u.is_counsellor)
def counsellor_home_view(request):
    notifications = CounsellorNotification.objects.filter(counsellor=request.user)
    return render(request, "accounts/counsellor_home.html", {"notifications": notifications})


@login_required
@user_passes_test(lambda u: u.is_agent)
def agency_home_view(request):
    notifications = AgentNotification.objects.filter(agency=request.user)
    return render(request, "accounts/agent_home.html", {"notifications": notifications})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "accounts/login.html", {"error": True})

    return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("accounts:login")


class AbstractRegisterView(View):
    user_form_class = RegForm
    info_form_class = None
    template_name = "accounts/register.html"
    current_page = ""

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        form = self.user_form_class()
        info_form = self.info_form_class()
        context = {"current": self.current_page, "form": form, "info_form": info_form}

        return render(request, self.template_name, context)

    @transaction.atomic
    def post(self, request):
        form = self.user_form_class(request.POST)
        info_form = self.info_form_class(request.POST)
        if form.is_valid() and info_form.is_valid():
            user = form.save(commit=False)
            user = self.set_role(user)
            user.save()

            user_info = info_form.save(commit=False)
            user_info.user = user
            user_info.save()
            self.save_many(info_form)
            return redirect("accounts:login")

        else:
            context = {"current": self.current_page, "form": form, "info_form": info_form}
            return render(request, self.template_name, context)

    def set_role(self, user):
        return user

    def save_many(self, form):
        pass


class StudentRegisterView(AbstractRegisterView):
    info_form_class = StudentRegForm
    current_page = "student"

    def set_role(self, user):
        user.is_student = True
        return user


class CounsellorRegisterView(AbstractRegisterView):
    info_form_class = CounsellorRegForm
    current_page = "counsellor"

    def set_role(self, user):
        user.is_counsellor = True
        user.is_active = False
        return user


class AgentRegisterView(AbstractRegisterView):
    info_form_class = AgencyRegForm
    current_page = "agent"

    def set_role(self, user):
        user.is_agent = True
        user.is_active = False
        return user

    def save_many(self, form):
        form.save_m2m()


def profile_view(request):
    return render(request, "accounts/profile.html")


class AbstractUpdateView(View):
    form_class = None
    password_form_class = PasswordChangeForm
    template_name = "accounts/profile.html"

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user.get_deatiled_instance())
        if form.is_valid():
            form.save()
            return redirect(request.path)
        else:
            password_form = self.password_form_class(user=request.user)
            return render(request, self.template_name, {"form": form, "password_form": password_form})

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("home")
        form = self.form_class(instance=request.user.get_deatiled_instance())
        password_form = self.password_form_class(user=request.user)
        return render(request, self.template_name, {"form": form, "password_form": password_form})


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("home")
        else:
            return render(request, "accounts/profile.html", {"password_form": password_form})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def verify_user_page(request):
    unverified_users = UserAccounts.objects.filter(is_active=False)
    return render(request, "accounts/verify_user.html", {"unverified_users": unverified_users})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def verify_user(request, id):
    user = UserAccounts.objects.get(id=id)
    user.is_active = True
    user.save()
    return redirect('/admin/verify/')

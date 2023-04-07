from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/verify/', views.verify_user_page),
    path('admin/verify/<int:id>/', views.verify_user),
    path('accounts/', include(("accounts.urls", "accounts"), namespace="accounts")),
    path('exam/', include(("exam.urls", "exam"), namespace="exam")),
    path('counsellor-agent/', include(("counsellor_agent.urls", "counsellor_agent"), namespace="counsellor_agent")),

    path('', views.home_view, name="home")
]

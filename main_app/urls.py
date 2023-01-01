from re import template
from django.urls import path
from .views import PasswordsChangeView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="Home"),
    path('login_superuser/', views.login_superuser, name="login_superuser"),
    path('login_admin/', views.login_admin, name="login_admin"),
    path('login_student/', views.login_student, name="login_student"),
    path('signup_student/', views.signup_student, name="signup_student"),
    path('book_app/', views.book_app, name="book_app"),
    path('book_app_student/', views.book_app_student, name="book_app_student"),
    path('book_app_alumni/', views.book_app_alumni, name="book_app_alumni"),
    path('css_form/', views.css_form, name="css_form"),
    path('admin_site/', views.admin_site, name="admin_site"),
    path('admin_site_sg/', views.admin_site_sg, name="admin_site_sg"),
    path('admin_site_re/', views.admin_site_re, name="admin_site_re"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create_manage/', views.create_manage, name="create_manage"),
    path('appointments/', views.appointments, name="appointments"),
    path('user/', views.user, name="user"),
    path('password/', PasswordsChangeView.as_view(template_name='change-password.html'), name="password"),
    path('logout_student/', views.logoutStudent, name="logout_student"),
    path('logout_admin/', views.logoutAdmin, name="logout_admin"),
    path('logout_superuser/', views.logoutSuperuser, name="logout_superuser"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="reset_password.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),

    path('generatePDF', views.generatePDF, name="generatePDF"),
    path('get_notif', views.notif, name="get_notif"),
    path('sdnotif', views.sd_notif, name="sdnotif"),

]
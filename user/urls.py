from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path("login/",views.login_user, name="login"),
    path("logout/",views.logout_user, name="logout"),
    path("register/",views.register_user, name="register"),

    #Profile Manage
    path("view_profile",views.view_profile, name="view_profile"),
    path("edit_profile",views.edit_profile, name="edit_profile"),
    path("delete_profile",views.delete_profile, name="delete_profile"),
    path("update_info",views.update_info, name="update_info"),

    #Change Password
    # Password Change
    path(
        'change_password/', 
        auth_views.PasswordChangeView.as_view(
            template_name='password_change_form.html'
        ), 
        name='change_password'
    ),
    path(
        'change_password_done/', 
        auth_views.PasswordChangeDoneView.as_view(
            template_name='password_change_done.html'
        ), 
        name='password_change_done'  # This name must match the one used in the view
    ),

   # Forget Password
    path(
        'password_reset/', 
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.html'
        ), 
        name='password_reset'
    ),
    path(
        'password_reset_done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ), 
        name='password_reset_done'
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'
        ), 
        name='password_reset_confirm'
    ),
    path(
        'password_reset_complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ), 
        name='password_reset_complete'
    ),
]

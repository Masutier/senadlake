from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *


urlpatterns = [
    path('registerUser', registerUser, name='registerUser'),
    path('userProfile', userProfile, name='userProfile'),

    path('loginPage', loginPage, name='loginPage'),
    path('userLogout', userLogout, name='userLogout'),

    path('password/reset_password/', auth_views.PasswordResetView.as_view(template_name='users/password/password_reset.html'), name='reset_password' ),
    path('password/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='users/password/password_reset_sent.html'), name='password_reset_done'),
    path('password/reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='users/password/password_reset_form.html'), name='password_reset_confirm'),
    path('password/reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password/password_reset_done.html'), name='password_reset_complete'),
]

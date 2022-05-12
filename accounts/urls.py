from django.urls import path
from . views import UserEditView, PasswordsChangeView, password_success, user_register, activate
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("register/", user_register, name="register"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path("password/", PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    #path("password/", auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path("password_success/", password_success, name="password_success"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        activate, name='activate'),
]

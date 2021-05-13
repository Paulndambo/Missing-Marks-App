from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from . forms import SignupForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None and user.student.id:
            auth.login(request, user)
            return redirect("data:profile")
        elif user is not None and user.lecturer.id:
            auth.login(request, user)
            return redirect("lecturers:lecturer_profile")
        else:
            messages.info(request, 'invalid creditials')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, "registration/password_success.html")

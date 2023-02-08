import secrets

from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView

from users.forms import CustomEditUserForm, CustomRegisterUserForm, CustomAuthenticationForm
from users.models import User
from users.services import confirm_account



class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm

def page_after_registration(request):
    return render(request, 'users/login_accept.html')
class CustomRegisterView(CreateView):
    model = User
    form_class = CustomRegisterUserForm
    success_url = '/users/page_after_registration/'


    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            self.object.is_active = False
            self.object.token = secrets.token_urlsafe(18)[:15]
            confirm_account(self.object)
            self.object.save()
        return super().form_valid(form)


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = '/'

    def get_object(self, queryset=None):
        return self.request.user



class CustomPasswordChangeView(PasswordChangeView):
    model = User
    success_url = '/'
    template_name = 'users/change_password.html'


def activate_user(request, token):
    u = User.objects.filter(token=token).first()

    if u:
        u.is_active = True
        u.save()
        return redirect('/users')

    return render(request, 'users/user_not_found.html')


def reset_password(request):
    if request.method == 'POST':

        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            mail = password_reset_form.cleaned_data['email']

            try:
                user = User.objects.get(email=mail)

            except Exception:
                user = False

            if user:
                new_password = User.objects.make_random_password(length=15)
                user.set_password(new_password)
                user.save()
                send_mail(
                    subject='Смена пароля',
                    message=f'Пароль успешно обновлен, для входа в аккаун используйте следующие дынные:\nПочта: {mail}\nПароль: {new_password}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[mail],
                    fail_silently=False
                )
                return redirect('users:login')

    return render(request, 'users/password_recovery.html')




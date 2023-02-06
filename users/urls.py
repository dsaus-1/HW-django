from django.contrib.auth.views import LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import CustomLoginView, UserEditProfileView, CustomRegisterView, CustomPasswordChangeView, \
    activate_user, reset_password, page_after_registration

app_name = UsersConfig.name



urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('page_after_registration/', page_after_registration, name='page_after_registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('register/', CustomRegisterView.as_view(), name='register'),
    path('password/', CustomPasswordChangeView.as_view(), name='password'),
    path('reset_password/', reset_password, name='reset_password'),
    path('activate/<str:token>/', activate_user, name='activate'),


]

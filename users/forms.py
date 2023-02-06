from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from catalog.forms_mixins import StyleFormMixin
from users.models import User


class CustomEditUserForm(StyleFormMixin, UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'avatar', 'phone', 'country')

class CustomRegisterUserForm(StyleFormMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'avatar', 'phone', 'country')

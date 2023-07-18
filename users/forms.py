from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import NMAUser

class NMAUserCreationForm(UserCreationForm):
    class Meta:
        model = NMAUser
        fields = ("email",)

class NMAUserChangeForm(UserCreationForm):
    class Meta:
        model = NMAUser
        fields = ("email",)
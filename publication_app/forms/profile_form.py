from django.contrib.auth.models import User
from django.forms import ModelForm


class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

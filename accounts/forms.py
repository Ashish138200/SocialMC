from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


# if both the class name and inherited class name are same than it will throw an error for self referencing class name
class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()  # Return the User model that is active in this project.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

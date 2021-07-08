from django.contrib.auth.forms import UserCreationForm

class CustomUserCreatorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)
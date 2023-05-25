from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CusomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age', )پ
        fields = ('username', 'age', 'email', 'first_name', 'last_name','nat_id', )
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser 
        fields = UserChangeForm.Meta.fields 
        
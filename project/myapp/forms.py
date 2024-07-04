from django import forms
from .models import BoardPost, Comment


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         # fields = '__all__'
#         exclude = (
#             "boardpost",
#             "user",
#         )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # 'post' 필드를 제외합니다.

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'PASSWORD'})
    )
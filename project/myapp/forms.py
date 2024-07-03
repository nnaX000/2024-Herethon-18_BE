from django import forms
from .models import BoardPost, Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = ('boardpost', 'user',)
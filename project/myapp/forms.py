from django import forms
from .models import BoardPost, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # fields = '__all__'
        exclude = (
            "boardpost",
            "user",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # 'post' 필드를 제외합니다.

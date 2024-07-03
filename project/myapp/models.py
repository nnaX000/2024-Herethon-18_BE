from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

class KakaoUser(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, blank=True)
    age_range = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nickname


class NaverUser(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100, blank=False)
    gender = models.CharField(max_length=10, blank=True)
    age_range = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nickname


class BoardPost(models.Model):
    DEVELOPMENT_PERIOD_CHOICES = [
        ("0-3", "0~3개월"),
        ("4-7", "4~7개월"),
        ("8-11", "8~11개월"),
        ("12+", "12개월 이상"),
    ]

    PARTICIPANTS_CHOICES = [
        ("1-6", "1~6명"),
        ("7-12", "7~12명"),
        ("13-18", "13~18명"),
        ("19+", "19명 이상"),
    ]

    LANGUAGE_CHOICES = [
        ("python", "Python"),
        ("numpy", "Numpy"),
        ("pandas", "Pandas"),
        ("java", "Java"),
        ("javascript", "JavaScript"),
        ("django", "Django"),
        ("html", "HTML"),
        ("css", "CSS"),
        ("c++", "C++"),
        ("other", "직접입력"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    development_period = models.CharField(
        max_length=5, choices=DEVELOPMENT_PERIOD_CHOICES
    )
    participants = models.CharField(max_length=6, choices=PARTICIPANTS_CHOICES)
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES)
    file = models.ImageField(upload_to="uploads/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name="liked_posts", blank=True)
    dislikes = models.ManyToManyField(User, related_name="disliked_posts", blank=True)

    def __str__(self):
        return self.title
    
    
from django.db import models
from django.conf import settings

class Comment(models.Model):
    boardpost = models.ForeignKey(BoardPost, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content


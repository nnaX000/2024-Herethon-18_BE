from django.contrib import admin
from django.urls import path, include
from myapp import views as v
from django.contrib.auth.views import LoginView
from myapp.views import AccountCreateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("board_create/", v.board_create, name='board_create'),
    path("board_list/", v.board_list, name='board_list'),
    path("accounts/", include("allauth.urls")),
    
    path("",LoginView.as_view(template_name='login.html'), name='login'),
    path('create/',AccountCreateView.as_view(), name='login_create'),
]

from django.contrib import admin
from django.urls import path, include
from myapp import views as v
from django.contrib.auth.views import LoginView
from myapp.views import AccountCreateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("board_create/", v.board_create, name="board_create"),
    path("board_list/", v.board_list, name="board_list"),
    path("accounts/", include("allauth.urls")),
    path("", LoginView.as_view(template_name="login.html"), name="login"),
    path("create/", AccountCreateView.as_view(), name="login_create"),
    path("", v.main, name="main"),
    path("board_create/", v.board_create, name="board_create"),
    path("login/", v.login, name="login"),
    path("board_list/", v.board_list, name="board_list"),
    path("accounts/", include("allauth.urls")),
    path("grow_1/", v.grow_1, name="grow_1"),
    path("like_post/<int:post_id>/", views.like_post, name="like_post"),
    path("dislike_post/<int:post_id>/", views.dislike_post, name="dislike_post"),
]

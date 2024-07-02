from django.contrib import admin
from django.urls import path, include
from myapp import views as v
from myapp.views import AccountCreateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("board_create/", v.board_create, name="board_create"),
    path("board_list/", v.board_list, name="board_list"),
    path("accounts/", include("allauth.urls")),
    path("create/", AccountCreateView.as_view(), name="login_create"),
    path("", v.main, name="main"),
    path("login/", v.login, name="login"),
    path("accounts/", include("allauth.urls")),
    path("grow_1/", v.grow_1, name="grow_1"),
    path("like_post/<int:post_id>/", views.like_post, name="like_post"),
    path("dislike_post/<int:post_id>/", views.dislike_post, name="dislike_post"),
    path("post/<int:post_id>/", v.board_detail, name="board_detail"),
    path("mypage_share/", v.mypage_share, name="mypage_share"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

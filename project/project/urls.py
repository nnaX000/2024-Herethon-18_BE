"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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
    path("board_create/", v.board_create, name="board_create"),
    path("login/", v.login, name="login"),
    path("board_list/", v.board_list, name="board_list"),
    path("accounts/", include("allauth.urls")),
    path("grow_1/", v.grow_1, name="grow_1"),
    path("like_post/<int:post_id>/", v.like_post, name="like_post"),
    path("dislike_post/<int:post_id>/", v.dislike_post, name="dislike_post"),
    path("post/<int:id>/", v.board_detail, name="board_detail"),  # URL이 올바른지 확인
    path("mypage_share/", v.mypage_share, name="mypage_share"),
    path("search/", v.search_view, name="search"),
    path("mypage/", v.mypage_setting, name="mypage_setting"),
    
    path("detail/<int:post_id>/", v.board_detail, name="board_detail"),
    path('detail/<int:post_id>/update/',v.update, name="update"),
    path('detail/<int:post_id>/delete/',v.delete, name="delete"),
    
    path('<int:pk>/comment/', v.comment_create, name='comment_create'),
    path('<int:article_pk>/comment/<int:comment_pk>/delete/', v.comment_delete, name='comment_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

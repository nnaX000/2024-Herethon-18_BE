from django.contrib import admin
from django.urls import path, include
from myapp import views as v

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", v.main),
    path("board_create/", v.board_create),
    path("board_list/", v.board_list),
    path("accounts/", include("allauth.urls")),
]

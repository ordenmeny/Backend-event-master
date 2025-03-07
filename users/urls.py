from django.contrib import admin
from django.urls import path, include, re_path
from .views import *

app_name = "users"

urlpatterns = [
    re_path(r'^auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('all-users/', ListUsersAPIView.as_view()),
    path('create-user/', RegisterUserAPIView.as_view()),
]

# 1)
# POST: users/auth/token/login/
# {
#     "username": <username>,
#     "password": <psw>
# }
# Ответ: данные из поля auth_token


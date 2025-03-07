from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from .serializers import *


class ListUsersAPIView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


class RegisterUserAPIView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)


    def create(self, request, *args, **kwargs):
        # Метод для регистрации пользователя через API (POST-запрос).
        # В БД сохраняется только uniq_code и введенные данные пользователя.
        # Создается токен для нового пользователя.
        # Возвращаются данные пользователя и токен.

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_active = True
        user.save()

        # Создаем токен для нового пользователя
        token, created = Token.objects.get_or_create(user=user)

        # Возвращаем данные пользователя и токен
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
        }, status=status.HTTP_201_CREATED)
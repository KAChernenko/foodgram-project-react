from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Модель юзера."""
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    username = models.CharField(
        max_length=150,
        verbose_name='username',
        unique=True,
        validators=(UnicodeUsernameValidator(), ))
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='email'
    )

    class Meta:
        ordering = ['username', ]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Follow(models.Model):
    """Модель подпсики на автора."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='following'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Подписчик',
        related_name='follower'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='unique_follow')]

    def __str__(self) -> str:
        return f'Пользователь {self.user} подписан на автора {self.author}'

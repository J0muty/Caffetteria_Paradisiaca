from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        if not login:
            raise ValueError("Users must have a login")
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(login, password, **extra_fields)

class RegUser(AbstractBaseUser):
    login = models.CharField('Логин', max_length=25, unique=True)
    password = models.CharField('Пароль', max_length=128)
    email = models.EmailField('Электронная почта', unique=True)
    firstname = models.CharField('Имя', max_length=25)
    lastname = models.CharField('Фамилия', max_length=25)
    birthday = models.DateField('День рождения', auto_now=False, auto_now_add=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email', 'firstname', 'lastname', 'birthday']
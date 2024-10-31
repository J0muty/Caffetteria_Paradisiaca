from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class RegUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Поле Email обязательно для заполнения')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class RegUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    birthdate = models.DateField('День рождения')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    dark_mode = models.BooleanField(default=False)

    general_emails = models.BooleanField(default=False)
    personalized_emails = models.BooleanField(default=False)

    objects = RegUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'birthdate']

    def __str__(self):
        return self.email


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(RegUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')])

    def __str__(self):
        return f"Order {self.id} - {self.user.email}"

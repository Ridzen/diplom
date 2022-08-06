from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class CustomManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            msg_ = ("Email not provided!")
            raise ValueError(msg_)
        email = self.normalize_email(email)
        user = self.model(
            email=email, **extra_fields
        )
        user.set_password(password)
        user.create_activation_code()
        user.save(
            using=self._db
        )
        return user

    def create_superuser(self, email, password, **extra_fields):
        if not email:
            msq_ = ('Email not provided!')
            raise ValueError(msq_)
        email = self.normalize_email(email)
        user = self.model(
            email=email, **extra_fields
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'male', 'male',
        FEMALE = 'female', 'female'

    username = None
    email = models.EmailField(
        unique=True, verbose_name='Почта'
    )
    full_name = models.CharField(
        verbose_name='Полное имя', max_length=200, blank=True, null=True
    )
    phone = models.CharField(
        verbose_name='Телефон', max_length=50
                             )
    avatar = models.ImageField(
        upload_to='avatars/', verbose_name='Аватар', null=True, blank=True
    )
    activation_code = models.CharField(
        max_length=25, blank=True, verbose_name='Код для активации'
    )
    is_active = models.BooleanField(
        default=False, verbose_name='Активный'
    )
    gender = models.CharField(
        max_length=32,
        verbose_name='Пол',
        choices=Gender.choices,
        default=Gender.MALE,
    )

    objects = CustomManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.email} -> {self.id}"

    def create_activation_code(self):
        code = get_random_string(
            length=10,
            allowed_chars='1234567890#$%!?_'
        )
        self.activation_code = code
        self.save(update_fields=['activation_code'])


class Email(models.Model):
    """
    for sending news to emails
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='send_emails', verbose_name='Пользователь'
    )

    def __str__(self):
        return self.user.email

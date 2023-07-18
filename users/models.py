from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from users.managers import NMAUserManager

# Create your models here.
class NMAUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    user_verified = models.BooleanField(default=False)
    admin_bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="staticfiles_build/images/")
    role = models.CharField(max_length=50)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('username',)

    objects = NMAUserManager()

    def __str__(self):
        return self.email

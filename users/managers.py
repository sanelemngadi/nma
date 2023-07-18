from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext as _

class NMAUserManager(BaseUserManager):
    """
    custom user manager where email is the unique identifyer
    for authentication instead of username
    """

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("users must have an email address"))

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("super user must have is_staff set to True"))

        if extra_fields.get(_("is_superuser")) is not True:
            raise ValueError(_("super user must have is_superuser set to True"))
        
        return self.create_user(email, password, **extra_fields)
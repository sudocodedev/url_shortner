from django.contrib.auth.models import AbstractUser
from django.db import models

from access.config import GenderChoices
from common.manager import UserManager
from common.models import COMMON_CHAR_MAX_LENGTH, COMMON_NULLABLE_BLANK_DEFAULT_CONFIG, BaseModel


class User(BaseModel, AbstractUser):
    """
    Contains the User details.

    ********************* Model Fields *********************
        Email       - email
        Char        - first_name, last_name
        Choices     - gender
        Bool        - is_admin
    """

    username = None
    first_name = models.CharField(max_length=COMMON_CHAR_MAX_LENGTH, **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)
    last_name = models.CharField(max_length=COMMON_CHAR_MAX_LENGTH, **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)
    email = models.EmailField(max_length=COMMON_CHAR_MAX_LENGTH, unique=True)
    gender = models.CharField(
        max_length=COMMON_CHAR_MAX_LENGTH,
        choices=GenderChoices.choices,
        **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG,
    )
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        default_related_name = "related_users"

    def __str__(self):
        return f"{self.id} - {self.email}"

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

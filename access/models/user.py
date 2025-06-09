from django.db import models
from django.contrib.auth.models import AbstractUser
from common.manager import UserManager
from common.models import BaseModel, COMMON_CHAR_MAX_LENGTH, COMMON_NULLABLE_BLANK_DEFAULT_CONFIG

class User(BaseModel, AbstractUser):
    """
    Contains the User details.

    ********************* Model Fields *********************
        Email       - email
        Char        - first_name, last_name 
    """

    username = None
    first_name = models.CharField(max_length=COMMON_CHAR_MAX_LENGTH, **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)
    last_name = models.CharField(max_length=COMMON_CHAR_MAX_LENGTH, **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)
    email = models.EmailField(max_length=COMMON_CHAR_MAX_LENGTH, unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        default_related_name = "related_users"

    def __str__(self):
        return f"{self.id} - {self.email}"
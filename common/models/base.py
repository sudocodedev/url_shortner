import uuid

from django.conf import settings
from django.db import models

from common.manager import BaseQuerySetManager
from common.models.config import COMMON_NULLABLE_BLANK_DEFAULT_CONFIG


class BaseModel(models.Model):
    """
    Abstract base model that provides common fields and behaviors for all models.
    ********************* Model Fields *********************
        PK          - id
        Unique      - uuid
        DateTime    - created, modified, deleted
        Bool        - is_active, is_deleted
        FK          - created_by, updated_by, deleted_by
    """

    # unique
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    # instance presence
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    # timestamp
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(**COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)

    # foreign keys
    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="created_%(class)s",
        on_delete=models.SET_DEFAULT,
        **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG,
    )
    updated_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="updated_%(class)s",
        on_delete=models.SET_DEFAULT,
        **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG,
    )

    deleted_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="deleted_%(class)s",
        on_delete=models.SET_DEFAULT,
        **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG,
    )

    objects = BaseQuerySetManager.as_manager()

    class Meta:
        abstract = True

import uuid

from django.conf import settings
from django.db import models

from common.manager import BaseQuerySetManager
from common.models import COMMON_NULLABLE_BLANK_DEFAULT_CONFIG


class BaseModel(models.Model):
    """"""

    #
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    #
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    #
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(**COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)

    #
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

from datetime import datetime

from django.db import models

from common.models import COMMON_CHAR_MAX_LENGTH, COMMON_NULLABLE_BLANK_DEFAULT_CONFIG, BaseModel


class URLMapping(BaseModel):
    """
    Contains the invoice details.

    ********************* Model Fields *********************
        DateTime    - last_accessed, expiry_tm
        Char        - short_code
        PositiveInt - access_count
    """

    short_code = models.CharField(
        max_length=COMMON_CHAR_MAX_LENGTH, unique=True, **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG
    )
    url = models.URLField(max_length=COMMON_CHAR_MAX_LENGTH, **COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)
    access_count = models.PositiveIntegerField(default=0)
    last_accessed = models.DateTimeField(**COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)
    expiry_tm = models.DateTimeField(**COMMON_NULLABLE_BLANK_DEFAULT_CONFIG)

    def update_stats(self):
        """
        Updates instance's
        - last_accessed with current time
        - increment access_count by 1
        """
        self.last_accessed = datetime.now()
        self.access_count += 1
        self.save()

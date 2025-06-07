from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist, ValidationError
from django.db.models import QuerySet
from django.utils import timezone


class BaseQuerySetManager(QuerySet):
    """"""

    def get_or_none(self, *args, **kwargs):
        """"""
        try:
            return super().get(*args, **kwargs)
        except (AttributeError, ValueError, ValidationError, MultipleObjectsReturned, ObjectDoesNotExist):
            return None

    def delete(self):
        """"""
        return super().update(is_active=False, is_deleted=True, deleted=timezone.now())

    def hard_delete(self):
        """"""
        return super().delete()

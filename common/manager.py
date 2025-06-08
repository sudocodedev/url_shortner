from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist, ValidationError
from django.db.models import QuerySet
from django.utils import timezone


class BaseQuerySetManager(QuerySet):
    """
    Custom QuerySet manager that extends Django's QuerySet to provide
    convenient methods for safe retrieval and soft/hard deletion.

    Methods:
        get_or_none(*args, **kwargs): Attempts to retrieve a single object matching the query.
            Returns the object if found, or None if not found or an exception occurs.

        delete(): Performs a soft delete on the queryset.
            Marks records as inactive, sets `is_deleted` to True, and timestamps the `deleted` field.

        hard_delete(): Permanently deletes records from the database.
            Calls the underlying `delete()` method to remove records.
    """

    def get_or_none(self, *args, **kwargs):
        """
        Retrieves a single object matching the given query parameters.
        Returns None if no object is found or if an error occurs (e.g., multiple objects found).
        """
        try:
            return super().get(*args, **kwargs)
        except (AttributeError, ValueError, ValidationError, MultipleObjectsReturned, ObjectDoesNotExist):
            return None

    def delete(self):
        """
        Performs a soft delete by updating the relevant fields on the queryset:
            - is_active = False
            - is_deleted = True
            - deleted = current timestamp
        """
        return super().update(is_active=False, is_deleted=True, deleted=timezone.now())

    def hard_delete(self):
        """Permanently deletes the records from the database."""
        return super().delete()

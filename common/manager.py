from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist, ValidationError
from django.db.models import QuerySet
from django.utils import timezone


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            email = input("Email: ")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("For super user, is_staff must be set to True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("For super user, is_superuser must be set to True")
        return self._create_user(email, password, **extra_fields)

    def get_or_none(self, *args, **kwargs):
        """
        Retrieves a single object matching the given query parameters.
        Returns None if no object is found or if an error occurs (e.g., multiple objects found).
        """
        try:
            return super().get(*args, **kwargs)
        except (ValueError, AttributeError, MultipleObjectsReturned, ObjectDoesNotExist, ValidationError):
            return None


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

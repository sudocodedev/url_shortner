from rest_framework import permissions


class NonAuthenticatedAPIMixin:
    """User can access API without any authentication"""

    permission_classes = [permissions.AllowAny]

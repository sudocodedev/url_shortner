from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from access.models import User
from access.serializers import (
    PasswordSerializer,
    UserInfoSerializer,
    UserProfileCUDSerializer,
    UserRegisterSerializer,
)
from common.mixins import NonAuthenticatedAPIMixin


class TokenBlackListAPIView(APIView):
    """Blacklist (invalidate) a refresh token."""

    def post(self, request, *args, **kwargs):
        """
        This is typically used to log a user out by making their refresh token unusable.
        Expects a POST request with a 'refresh' token in the request body.
        """
        refresh = request.data.get("refresh")
        if not refresh:
            return Response({"error": ["Refresh token required."]}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh)
            token.blacklist()
            return Response({"success": ["Logout successfull."]}, status=status.HTTP_200_OK)
        except (TokenError, InvalidToken):
            return Response({"error": ["Invalid refresh token."]}, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterViewSet(NonAuthenticatedAPIMixin, CreateModelMixin, GenericViewSet):
    """View for registering users"""

    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserProfileAPIView(APIView):
    """user profile view"""

    def get(self, request, *args, **kwargs):
        """Get logged in user profile"""
        serializer = UserInfoSerializer(instance=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        """Update user profile"""
        user = request.user
        serializer = UserProfileCUDSerializer(user, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """Delete user instance"""
        user = request.user
        user.delete()
        return Response({"success": ["Profile Deleted."]}, status=status.HTTP_204_NO_CONTENT)



class SetPasswordAPIView(APIView):
    """View to set password for user profile for authenticated user"""

    def post(self, request, *args, **kwargs):
        """User can set password in their profile"""
        user = request.user
        serializer = PasswordSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        password = serializer.validated_data.pop("password")
        if user.check_password(password):
            return Response({"error": ["New password can't be same as old password."]}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(password)
        user.save()
        return Response({"success": ["Password set successfully."]}, status=status.HTTP_200_OK)

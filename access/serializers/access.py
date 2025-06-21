from rest_framework import serializers

from access.config import GenderChoices
from access.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    gender = serializers.ChoiceField(choices=GenderChoices)
    is_admin = serializers.BooleanField(default=False, required=False)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "gender", "is_admin", "password"]

    def create(self, validated_data):
        """Creating user and setting their password"""
        password = validated_data.pop("password", None)
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class UserInfoSerializer(serializers.ModelSerializer):
    """Read only serializer for User"""

    class Meta:
        model = User
        fields = ["id", "uuid", "first_name", "last_name", "email", "gender", "is_admin"]

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, validated_data):
        raise NotImplementedError


class UserProfileCUDSerializer(serializers.ModelSerializer):
    """CUD Serializer for user profile"""

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "gender"]

    def update(self, instance, validated_data):
        """validation check for email during updation"""
        email = validated_data.get("email")
        if User.objects.filter(email=email).exclude(id=instance.id).exists():
            raise serializers.ValidationError({"error": ["Email already exists."]})
        return super().update(instance, validated_data)


class PasswordSerializer(serializers.Serializer):
    """serializer for password"""

    password = serializers.CharField(write_only=True, style={"input_type": "password"})

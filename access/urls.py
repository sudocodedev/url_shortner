
from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from access.views import SetPasswordAPIView, TokenBlackListAPIView, UserProfileAPIView, UserRegisterViewSet

app_name = "access"

API_URL_PREFIX = "api/access"

router = routers.DefaultRouter()

router.register(f'{API_URL_PREFIX}/register', UserRegisterViewSet)

urlpatterns = [
    path(f'{API_URL_PREFIX}/login/', TokenObtainPairView.as_view()),
    path(f'{API_URL_PREFIX}/login/refresh/', TokenRefreshView.as_view()),
    path(f'{API_URL_PREFIX}/logout/', TokenBlackListAPIView.as_view()),
    path(f'{API_URL_PREFIX}/profile/', UserProfileAPIView.as_view()),
    path(f'{API_URL_PREFIX}/profile/password/set/', SetPasswordAPIView.as_view()),
] + router.urls

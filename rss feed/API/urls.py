from django.urls import path
from .views.account_views import *
urlpatterns = [
    path("register", RegisterAPIView.as_view()),
    path("login", LoginAPIView.as_view()),
    path("account", AccountAPIView.as_view()),
    path("refresh", RefreshAPIView.as_view()),
    path("logout", LogoutAPIView.as_view()),
]

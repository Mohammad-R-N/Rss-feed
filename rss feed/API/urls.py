from django.urls import path
from .views.account_views import *
from .views.podcast_views import *

urlpatterns = [
    path("register", RegisterAPIView.as_view(),name="register"),
    path("login", LoginAPIView.as_view(),name="login"),
    path("account", AccountAPIView.as_view(),name="account"),
    path("refresh", RefreshAPIView.as_view(),name="refresh"),
    path("logout", LogoutAPIView.as_view(),name="logout"),
    path("podcasts/", ChannelListCreateView.as_view(), name="podcast-list-create"),
    path("podcasts/<int:pk>/", ChannelDetailView.as_view(), name="podcast-detail"),
    path("podcasts/<int:pk>/episodes/",EpisodeListCreateView.as_view(),name="podcast-episodes-list-create",),
    path("episodes/<int:pk>/", EpisodeDetailView.as_view(), name="episode-detail"),
]

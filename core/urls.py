from django.urls import path

from .views import test_view, PostView,PostCreateApi
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', PostCreateApi.as_view()),
    path('api/token/', obtain_auth_token, name='obtain-token'),
]
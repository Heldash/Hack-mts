from django.urls import path
from .views import AllUsers

urlpatterns = [
    path("all_users",AllUsers.as_view(),name="get_all_users")
]
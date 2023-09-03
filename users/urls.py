
from django.urls import path
from .views import UserView,UsersList
urlpatterns=[
 path("register",UserView.as_view(),name="registration"),
 path("list",UsersList.as_view(),name="list-all"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("account/<int:id>", views.account, name="account"),
]
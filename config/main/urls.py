from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("choose/", views.choose, name="choose"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("worker/", views.worker, name="worker"),
    path("client/", views.client, name="client"),

]



    
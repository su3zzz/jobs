from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("choose/", views.choose, name="choose"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("worker/", views.worker, name="worker"),
    path("client/", views.client, name="client"),
    path("talents/", views.talents, name="talents"),
    path("messages/", views.messages, name="messages"),
    path("workerjobs/", views.workerjobs, name="workerjobs"),
    path("profile/", views.profile, name="profile"),
    path("profile2/", views.profile2, name="profile2"),
    path("payment/", views.payment, name="payment"),
]



    
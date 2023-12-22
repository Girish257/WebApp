from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("abc/", views.abc, name="abc"),
    path("new/", views.new, name="new"),
    path("two/", views.two, name="two"),
    path("thankyou/", views.thankyou, name="thankyou"),
]
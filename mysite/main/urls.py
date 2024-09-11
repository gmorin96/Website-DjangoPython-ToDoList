from django.urls import path
from . import views
#from register import views as reg_views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("<int:id>", views.index, name="index"),
]
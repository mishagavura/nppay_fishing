

from django.urls import path

from django.contrib.auth import views as auth_views 
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('tracking/?cargo_number=20450271329485', views.login_in, name="login")
]

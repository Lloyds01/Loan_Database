
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('bvn_check/', internal_check.as_view()),
    path('logout/', user_logout),
]

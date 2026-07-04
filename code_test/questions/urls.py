from django.urls import path
from .views import *

app_name = "questions"
urlpatterns = [
    # shop order page
    path("", questions, name="questions"),
]

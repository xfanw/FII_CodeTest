from django.urls import path
from .views import *

app_name = "questions"
urlpatterns = [
    # shop order page
    path("", questions, name="questions"),
    path("question1", question1, name="question1"),
    path("question2", question2, name="question2"),
]

from django.urls import path
from .views import *
from .view_no_change import questions, reset_employee

app_name = "questions"

urlpatterns = [
    path("", questions, name="questions"),
    path("reset_employee", reset_employee, name="reset_employee"),
    path("delete_emp", delete_emp, name="delete_emp"),
]

urlpatterns += [
    path("question1", question1, name="question1"),
    path("question2", question2, name="question2"),
    path("question3", question3, name="question3"),
]

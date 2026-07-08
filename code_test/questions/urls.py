from django.urls import path
from .views import *
from .view_no_change import questions, reset_employee

app_name = "questions"

urlpatterns = [
    path("", questions, name="questions"),
    path("reset_employee", reset_employee, name="reset_employee"),
]

urlpatterns += [
    path("question1", question1, name="question1"),
    path("question2", question2, name="question2"),
    path("question3", question3, name="question3"),
    path("question3/delete_emp", question3_delete_emp, name="question3_delete_emp"),
    path("question4", question4, name="question4"),
]

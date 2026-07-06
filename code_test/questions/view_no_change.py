# DO NOT Change this file
from django.shortcuts import render
from core.RawDB import reset_index
from core.app_functions import json_success
from questions.models import Employee


def questions(request):
    context = {}
    return render(request, "questions/questions.html", context)


def reset_employee(request):
    Employee.objects.all().delete()
    reset_index(["questions_employee"])
    emp_list = [
        Employee(first_name="Emma", last_name="Carter"),
        Employee(first_name="Liam", last_name="Brooks"),
        Employee(first_name="Sophia", last_name="Turner"),
        Employee(first_name="Noah", last_name="Bennett"),
        Employee(first_name="Olivia", last_name="Mitchell"),
        Employee(first_name="Ethan", last_name="Collins"),
        Employee(first_name="Ava", last_name="Parker"),
        Employee(first_name="Mason", last_name="Reed"),
        Employee(first_name="Isabella", last_name="Cooper"),
        Employee(first_name="Lucas", last_name="Foster"),
        Employee(first_name="Mia", last_name="Richardson"),
    ]
    Employee.objects.bulk_create(emp_list)
    return json_success()

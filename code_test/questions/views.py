from django.shortcuts import render

from core.app_functions import json_success
from questions.models import Employee


def question1(request):
    context = {}
    return render(request, "questions/question1.html", context)


def question2(request):
    context = {}
    return render(request, "questions/question2.html", context)


def question3(request):
    context = {"emp_list": Employee.objects.all()}
    return render(request, "questions/question3.html", context)


def question3_delete_emp(request):
    my_id = request.GET.get("emp_id")
    Employee.objects.filter(id=my_id).delete()
    return json_success()


def question4(request):
    context = {"emp_list": Employee.objects.all()}
    return render(request, "questions/question4.html", context)

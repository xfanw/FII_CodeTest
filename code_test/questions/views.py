from django.shortcuts import render
from core.app_functions import json_error, json_success
from questions.models import Employee
from django.contrib import messages


def info():
    messages.success()
    json_success()
    json_error()


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

    search_val = request.GET.get("search_val")

    if search_val:
        context["curr_search"] = search_val
        messages.error(request, f"Your search value is {search_val}")
        # hint: write your code for question 4 here
        # from django.db.models import Q  # as needed

    return render(request, "questions/question4.html", context)


def question5(request):
    context = {"emp_list": Employee.objects.all()}

    return render(request, "questions/question5.html", context)

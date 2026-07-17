from django.shortcuts import render
from core.app_functions import json_error, json_success
from questions.models import Employee
from django.contrib import messages
from django.views import View


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


def question5_add_employee(request):
    first_name = request.GET.get("first_name")
    last_name = request.GET.get("last_name")
    # check if employee with same first_name and last_name already exists, if not, create new employee
    if first_name and last_name:
        # Add new employee if not exists
        return json_success(f"Employee {first_name} {last_name} added successfully.")

    return json_error("You have to input both first name and last name. ")


class Question6(View):
    template_name = "questions/question6.html"

    def get(self, *args, **kwargs):
        context = {"emp_list": Employee.objects.all()}
        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        context = {"emp_list": Employee.objects.all()}
        first_name = self.request.POST.getlist("first_name")
        last_name = self.request.POST.getlist("last_name")

        # Modify the following section to save multiple employees at once
        if first_name and last_name:
            # Add new employee if not exists

            messages.success(self.request, f"Employee {first_name} {last_name} added successfully.")
            return render(self.request, self.template_name, context)

        messages.error(self.request, "You have to input both first name and last name. ")
        return render(self.request, self.template_name, context)

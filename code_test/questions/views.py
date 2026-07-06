from django.shortcuts import render


# Create your views here.
def questions(request):
    context = {}
    return render(request, "questions/questions.html", context)


def question1(request):
    context = {}
    return render(request, "questions/question1.html", context)


def question2(request):
    context = {}
    return render(request, "questions/question2.html", context)


def question3(request):
    context = {}
    return render(request, "questions/question3.html", context)

from django.shortcuts import render


# Create your views here.
def questions(request):
    context = {}
    return render(request, "questions/questions.html", context)

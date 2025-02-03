from django.shortcuts import render
from .models import Question


def index(request):
    questions = Question.objects.all()  # Получаем все вопросы из базы
    return render(request, 'main/main.html', {'questions': questions})


def faqs(request):
    return render(request, 'main/faqs.html')


def about(request):
    return render(request, 'main/about.html')
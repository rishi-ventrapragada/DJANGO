# WEEK7: Create a Quiz Application using Django Framework along with SQLite3.

# views.py
from django.shortcuts import render
from .models import Question, Choice


def quiz_view(request):
    questions = Question.objects.all()
    return render(request, "quiz/quiz.html", {"questions": questions})


def result_view(request):
    if request.method == "POST":
        score = 0
        questions = Question.objects.all()
        for question in questions:
            # Each question's input name should be its ID in the template
            selected = request.POST.get(str(question.id))
            if selected:
                try:
                    choice = Choice.objects.get(id=int(selected), question=question)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

        return render(request, "quiz/result.html", {
            "score": score,
            "total": questions.count()
        })
    else:
        # If someone visits result_view directly without POST
        return render(request, "quiz/result.html", {
            "score": 0,
            "total": 0
        })

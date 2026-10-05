# WEEK6: Demonstrate Cache, Session Management for Student Login Application.

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from .models import Student


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 1 Check cache first
        student = cache.get(username)
        if not student:
            try:
                student = Student.objects.get(username=username)
                cache.set(username, student, timeout=300)  # cache for 5 mins
            except Student.DoesNotExist:
                return HttpResponse("Invalid username")

        # 2 Validate password
        if student.check_password(password):
            # 3 Create session
            request.session["student_id"] = student.id
            request.session["username"] = student.username

            # 4 Create cookie
            response = HttpResponse(f"Welcome {student.username}!")
            response.set_cookie("student_username", student.username, max_age=3600)
            return response
        else:
            return HttpResponse("Invalid password")

    return render(request, "login.html")


#dashboard
def dashboard_view(request):
    if "student_id" in request.session:
        return HttpResponse(f"Welcome {request.session['username']}! <a href='/logout/'>Logout</a>")
    else:
        return HttpResponse("Please login first.")


#logout
def logout_view(request):
    # Clear session
    request.session.flush()

    # Clear cookie
    response = HttpResponse("Logged out successfully!")
    response.delete_cookie("student_username")
    return response

from django.http.response import JsonResponse
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.


def home(request):
    form = StudentRegistration()
    students = User.objects.all()
    return render(request, "crud/home.html", {"form": form, "students": students})


def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            stuid = request.POST["stuid"]
            university_id = request.POST["university_id"]
            name = request.POST["name"]
            semester = request.POST["semester"]
            phone_number = request.POST["phone_number"]

            if stuid == "":
                user = User(
                    university_id=university_id,
                    name=name,
                    semester=semester,
                    phone_number=phone_number,
                )
            else:
                user = User(
                    id=stuid,
                    university_id=university_id,
                    name=name,
                    semester=semester,
                    phone_number=phone_number,
                )

            user.save()

            latest_students = list(User.objects.values())

            return JsonResponse({"status": "Saved", "latest_students": latest_students})
        else:
            return JsonResponse({"status": 0})


def delete_data(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        user = User.objects.get(pk=id)
        user.delete()

        return JsonResponse({"status": 1})
    else:
        return JsonResponse({"status": 0})


def edit_data(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        student = User.objects.get(pk=id)
        student_data = {
            "id": student.id,
            "university_id": student.university_id,
            "name": student.name,
            "semester": student.semester,
            "phone_number": student.phone_number,
        }
        return JsonResponse(student_data)

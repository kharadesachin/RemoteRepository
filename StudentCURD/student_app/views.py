from django.shortcuts import render, redirect
from .models import Student


def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def add_stud(request):
    return render(request, 'add_stud.html')


def stud_added(request):
    first_name1 = request.POST.get('fname')
    last_name1 = request.POST.get('lname')
    section_name1 = request.POST.get('section')
    class_name1 = request.POST.get('class')
    school_name1 = request.POST.get('school')
    mobile1 = request.POST.get('mobile')
    marathi1 = request.POST.get('marathi')
    english1 = request.POST.get('english')
    hindi1 = request.POST.get('hindi')
    maths1 = request.POST.get('maths')
    science1 = request.POST.get('science')
    social1 = request.POST.get('social')

    data = Student(
        first_name=first_name1,
        last_name=last_name1,
        section_name=section_name1,
        class_name=class_name1,
        school_name=school_name1,
        mobile=mobile1,
        marathi_marks=marathi1,
        english_marks=english1,
        hindi_marks=hindi1,
        maths_marks=maths1,
        science_marks=science1,
        social_marks=social1
    )
    data.save()

    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def update_stud(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'update.html', {'student': student})


def delete_stud(request, pk):
    stud = Student.objects.get(id=pk)
    stud.delete()

    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})


def stud_updated(request, pk):
    stud = Student.objects.get(id=pk)

    stud.first_name = request.POST.get('fname')
    stud.last_name = request.POST.get('lname')
    stud.section_name = request.POST.get('section')
    stud.class_name = request.POST.get('class')
    stud.school_name = request.POST.get('school')
    stud.mobile = request.POST.get('mobile')
    stud.marathi_marks = request.POST.get('marathi')
    stud.english_marks = request.POST.get('english')
    stud.hindi_marks = request.POST.get('hindi')
    stud.maths_marks = request.POST.get('maths')
    stud.science_marks = request.POST.get('science')
    stud.social_marks = request.POST.get('social')

    stud.save()

    return redirect("/")
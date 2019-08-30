from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home/home_new.html')
def about(request):
    return render(request,'home/about.html')
def announcements(request):
    return render(request,'home/announcements.html')
def course_ms(request):
    return render(request,'home/course_ms.html')
def course_mtech(request):
    return render(request,'home/course_mtech.html')
def course_phd(request):
    return render(request,'home/course_phd.html')
def facilities(request):
    return render(request,'home/facilities.html')
def faculty(request):
    return render(request,'home/faculty.html')
def project_dyslexia(request):
    return render(request,'home/project_dyslexia.html')
def project_ide(request):
    return render(request,'home/project_ide.html')
def project_nptel(request):
    return render(request,'home/project_nptel.html')
def project_pedagogy(request):
    return render(request,'home/project_pedagogy.html')
def projects(request):
    return render(request,'home/projects.html')
def research_areas(request):
    return render(request,'home/research_areas.html')
def staff(request):
    return render(request,'home/staff.html')
def students(request):
    return render(request,'home/students.html')

from django.shortcuts import render
from exercises.models import Project

# Create your views here.
def exercise_index(request):
    projects = Project.objects.all()

    context = {
       'projects': projects ,
    }
    return render(request, 'exercise_index.html', context)

def exercise_category(request, category):
    projects = Project.objects.filter(
        categories__name__contains=category
    )
    context = {
        "category": category,
        "projects": projects,
    }
    return render(request, "exercise_category.html", context)

def exercise_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'exercise_detail.html', context)
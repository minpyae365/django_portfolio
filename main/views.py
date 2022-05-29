from django.shortcuts import render
from main.models import Project, Intro, Contact

# Create your views here.
def home(request):
    projects = Project.objects.all()
    contacts = Contact.objects.all()
    if Intro( name='Steven' ):
        intro = Intro.objects.get()
    else:
        intro = None
    context = {
       'projects': projects ,
       'intro' : intro,
       'contacts' : contacts,
    }
    return render(request, 'home.html', context)

def project_category(request, category):
    projects = Project.objects.filter(
        categories__name__contains=category
    )
    context = {
        "category": category,
        "projects": projects
    }
    return render(request, "project_category.html", context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

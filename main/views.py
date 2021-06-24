from django.shortcuts import render

# Create your views here.


def homePage(request):
    context = {
        'title': 'World'
    }
    return render(request, 'homepage.html', context)

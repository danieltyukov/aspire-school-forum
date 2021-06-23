from django.shortcuts import render

# Create your views here.


def homePage(request):
    context = {
        'title': 'World'
    }
    return render(request, 'homePage.html', context)

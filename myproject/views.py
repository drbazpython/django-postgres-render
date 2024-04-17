from django.shortcuts import render

def homepage(request):
    #return HttpResponse("Home Page")
    return render(request, 'home.html')

def aboutpage(request):
    #return HttpResponse("About Page")
    return render(request, 'about.html')
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def landing_page(request):
    return redirect('/home/')

def about(request):
    html = """
    <h1>Hi this is Abhiaji</h1>
    """
    return HttpResponse(html)

def sign_up(request):
    return render(request, 'sign_up.html')

def error(request, exception):
    return render(request, 'error.html')

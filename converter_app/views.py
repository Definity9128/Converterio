from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse('<h1>Welcome to Converter.io</h1>')

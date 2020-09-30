from django.shortcuts import render

# Create your views here.

def index(request):
    try:
        print('hi,,')
        return render(request, "base.html")
    except Exception as e:
        print(e.args)

def login(request):
    try:
        print('login')
    except Exception as e:
        print(e.args)


def register(request):
    try:
        print('signup')
    except Exception as e:
        print(e.args)
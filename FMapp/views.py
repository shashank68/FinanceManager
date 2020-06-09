from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request, 'index.html', {'name': 'Sha68'})

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        pswrd = request.POST['password']


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        email = request.POST['email']
        pswrd1 = request.POST['password1']
        pswrd2 = request.POST['password2']

        if pswrd1 == pswrd2:
            if User.objects.filter(email=email).exists():
                # email exists
            else:
                user = User.objects.create_user(username = email, email = email, password = pswrd2)
                user.save()
        else:
            # invalid psswrd
        return redirect('/')
    
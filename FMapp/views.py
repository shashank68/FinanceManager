from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from plotly.offline import plot
from plotly.graph_objs import Scatter
from .models import Stocks
# Create your views here.


def index(request):
    return render(request, 'index.html', {'name': 'Sha68'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST['email']
        pswrd = request.POST['password']
        user = auth.authenticate(username=email, password=pswrd)
        if user is not None:
            auth.login(request, user)
            return redirect('/stocks')
        else:
            messages.info(request, 'No user')
            return redirect('/login')

def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        email = request.POST['email']
        pswrd1 = request.POST['password1']
        pswrd2 = request.POST['password2']
        emailTaken = False

        if pswrd1 == pswrd2:

            if User.objects.filter(email=email).exists():
                messages.info(request, 'email is associated with an account')
                emailTaken = True
                return redirect('/register', {'emailTaken': emailTaken})
            else:
                user = User.objects.create_user(
                    username=email, email=email, password=pswrd2)
                user.save()
        else:
            messages.info(request, "Passwords doesn't match")
            return redirect('/register')
        return redirect('/')

# def grph(request):
#     x_data = [0,1,2,3]
#     y_data = [x**3 for x in x_data]
#     plot_div = plot([Scatter(x=x_data, y=y_data, mode='lines', name='test', opacity=0.8, marker_color='green')], output_type='div', include_plotlyjs=False, show_link=False, link_text="")
#     return render(request, 'grph.html', context={'plot_div': plot_div})
def stocks(request):

    # stocks = Stocks.objects.all()
    return render(request, 'stocks.html')

def newStockEntry(request):
    if request.method == 'GET':
        return render(request, 'newStockEntry.html')
    else:
        comp_name = request.POST['company_name']
        comp_sym = request.POST['company_symbol']
        purchase_date = request.POST['purchase_date']
        purchase_cost = request.POST['purchase_cost']
        quantity = request.POST['quantity']

        request.user.stocks.create(Company_Name=comp_name, Company_Symbol = comp_sym, Purchase_Date = purchase_date, Purchase_Cost = purchase_cost, Quantity = quantity)
        return render(request, 'stocks.html')




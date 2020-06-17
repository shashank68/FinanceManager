from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from plotly.offline import plot
# from plotly.graph_objs import Scatter
from .models import Stocks, Savings
from django.contrib.auth.decorators import login_required
import yfinance as yf
import plotly.express as px
from plotly.offline import plot

# Create your views here.


def index(request):
    return render(request, 'index.html')


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


@login_required(login_url='/login')
def showstock(request, company_symbol):
    
    share_data = yf.Ticker(company_symbol).history(period="1mo")
    figures = px.line(x=share_data.index, y=share_data.Close, labels={'x':'Date', 'y':'Closing Price'})
    figures.update_layout(
        height=850,
    )
    figures.update_yaxes(automargin=True)
    figures.update_xaxes(automargin=True)
    output_div = plot(figures, output_type='div', show_link= False, link_text="", include_plotlyjs=False)
    print(output_div)
    return render(request, "showstock.html", {'plot_div': output_div, 'comp_sym': company_symbol})




@login_required(login_url='/login')
def stocks(request):
    return render(request, 'stocks.html')



@login_required(login_url='/login')
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


@login_required(login_url='/login')
def savings(request):
    return render(request, 'savings.html')

@login_required(login_url='/login')
def newsaving(request):
    if request.method == 'GET':
        return render(request, 'newSavingEntry.html')
    else:
        bank_name = request.POST['bank_name']
        account_num = request.POST['account_num']
        balance = request.POST['balance']

        request.user.savings.create(Bank_Name=bank_name, Account_Number = account_num, Balance = balance, Status = True)
        return render(request, 'savings.html')



@login_required(login_url='/login')
def loans(request):
    return render(request, 'loans.html')

@login_required(login_url='/login')
def newloan(request):
    if request.method == 'GET':
        return render(request, 'newLoanEntry.html')
    else:
        bank_name = request.POST['bank_name']
        account_num = request.POST['account_num']
        balance = request.POST['balance']

        request.user.loans.create(Bank_Name=bank_name, Account_Number = account_num, Balance = balance, Status = True)
        return render(request, 'loans.html')

from django.shortcuts import render,redirect
from inuamkulimaApp.models import Member


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def consultation(request):
    return render(request,'consultation.html')
def contact(request):
    return render(request,'contact.html')



def form(request):
        if request.method == "POST":
            members = Member(
                email=request.POST['email'],
                password=request.POST['password']
            )
            members.save()
            return redirect('/login')
        else:
            return render(request, 'form.html')
def loan(request):
    return render(request,'loan.html')
def login(request):
    return render(request,'login.html')
def market(request):
    return render(request,'market.html')
def question(request):
    return render(request,'question.html')
def weather(request):
    return render(request,'weather.html')
def services(request):
    return render(request,'services.html')
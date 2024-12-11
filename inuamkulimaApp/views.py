import json
from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse


from inuamkulimaApp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from inuamkulimaApp.models import Member,ImageModel,loan
from inuamkulimaApp.forms import  ImageUploadForm

# Create your views here.
from django.shortcuts import render, redirect
from inuamkulimaApp.models import Member


def index(request):
    return render(request, 'index.html')
 # if request.method == 'POST':
 #     if Member.objects.filter(
 #             email=request.POST['email'],
 #             password=request.POST['password']
 #     ).exists():
 #         member = Member.objects.get(
 #           email = request.POST['email'],
 #           password = request.POST['password'],
 #         )
 #         return render(request,'index.html',{'members':member})
 #
 #     else:
 #         return render(request,'login.html')
 # else:
 #     return render(request,'login.html')

def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def starter(request):
    return render(request, 'starter-page.html')
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
            return redirect('/index')
        else:
            return render(request, 'form.html')
def loan(request):
    return render(request,'loan.html')
# def login(request):
#     return render(request,'login.html')
# from django.shortcuts import redirect


def login(request):
    return render(request, 'login.html')
    # if request.method == 'POST':
    #     email = request.POST['email'],
    #     password = request.POST['password']
    #
    #     # Check if member exists
    #     if Member.objects.filter(email=email, password=password).exists():
    #         member = Member.objects.get(email=email, password=password)
    #
    #         # Set session or any required logic
    #         request.session['member_id'] = member.id  # Example: Store user ID in session
    #
    #         # Redirect to the index page
    #         return redirect('index')  # Replace 'index' with the name of your URL pattern
    #     else:
    #         return render(request, 'login.html', {'error': 'Invalid credentials'})
    #
    # # For GET requests, show the login page
    # return render(request, 'login.html')


def market(request):
    return render(request,'market.html')
def question(request):
    return render(request,'question.html')

def weather(request):
    return render(request,'weather.html')
def incentives(request):
    return render(request,'incentives.html')
def trainings(request):
    return render(request,'trainings.html')
def service(request):
    return render(request,'services.html')
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')
def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")

def show(request):
    information = loan.objects.all()
    return render(request, 'show.html', {'data': information})
def delete(request, id):
    contacts = contact.objects.get(id=id)
    contacts.delete()
    return redirect('/show')


def edit(request, id):
    appointment = contact.objects.get(id=id)
    return render(request, 'edit.html', {'x': appointment})
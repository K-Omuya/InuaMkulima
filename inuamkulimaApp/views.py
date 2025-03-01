import json
from pyexpat.errors import messages
from requests.auth import HTTPBasicAuth
import requests
from django.http import HttpResponse
from django.contrib.auth.models import User
from inuamkulimaApp.credentials import MpesaAccessToken, LipanaMpesaPpassword


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username or not password:
            messages.error(request, "Username and password are required.")
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')

    return render(request, 'login.html')


from django.contrib.auth import authenticate, login

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # Check if any field is empty
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect('register')

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')

    return render(request, 'user_register.html')



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'login.html')


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

def landing(request):
    return render(request,'landing.html')
def about(request):
    return render(request,'about.html')
def starter(request):
    return render(request, 'starter-page.html')
def consultation(request):
    return render(request, 'request_consultation.html')
def contact(request):
    return render(request,'contact.html')


def loan(request):
    return render(request, 'loan_application.html')
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
    return render(request, 'marketplace.html')
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


















from django.shortcuts import render, redirect
from .models import ContactMessage
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def manage(request):
    return render(request, 'manage.html')
def messages_list(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'messages_list.html', {'messages': messages})

def delete_message(request, message_id):
    message = ContactMessage.objects.get(id=message_id)
    message.delete()
    return redirect('messages_list')

from django.shortcuts import render, redirect, get_object_or_404
from .models import TrainingSession
from .forms import TrainingSessionForm

def training_sessions(request):
    sessions = TrainingSession.objects.all()
    form = TrainingSessionForm()

    if request.method == "POST":
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_sessions')

    return render(request, 'trainings.html', {'sessions': sessions, 'form': form})

def delete_session(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)
    session.delete()
    return redirect('training_sessions')


def edit_training_session(request, session_id):
    session = get_object_or_404(TrainingSession, id=session_id)

    if request.method == "POST":
        form = TrainingSessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('training_sessions')  # Redirect to the sessions list
    else:
        form = TrainingSessionForm(instance=session)

    return render(request, 'edit_training_session.html', {'form': form, 'session': session})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ConsultationRequest

from django.shortcuts import render, redirect
from .forms import ConsultationRequestForm
from .models import ConsultationRequest



from django.shortcuts import render, redirect
from .forms import ConsultationRequestForm
from .models import ConsultationRequest

def request_consultation(request):
    if request.method == "POST":
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("consultation_success")  # Redirect after submission
    else:
        form = ConsultationRequestForm()

    return render(request, "request_consultation.html", {"form": form})


from django.contrib.auth.decorators import login_required

@login_required
def user_consultations(request):
    consultations = ConsultationRequest.objects.filter(email=request.user.email)
    return render(request, "user_consultations.html", {"consultations": consultations})

@login_required
def manage_consultations(request):
    if not request.user.is_staff:
        return redirect('home')

    requests = ConsultationRequest.objects.all()
    return render(request, 'manage_consultations.html', {'requests': requests})

@login_required
def approve_consultation(request, request_id):
    consultation = get_object_or_404(ConsultationRequest, id=request_id)
    consultation.status = 'approved'
    consultation.consultation_date = request.POST.get('consultation_date')
    consultation.save()
    return redirect('manage_consultations')

@login_required
def deny_consultation(request, request_id):
    consultation = get_object_or_404(ConsultationRequest, id=request_id)
    consultation.status = 'denied'
    consultation.save()
    return redirect('manage_consultations')



import random
from django.shortcuts import render
from inuamkulimaApp.models import Product

import random
from django.shortcuts import render
from .models import Product

def marketplace(request):
    # Get search query and category filter from request
    search_query = request.GET.get('search', '').strip()
    category_filter = request.GET.get('category', 'All').strip()

    # Fetch all products
    products = Product.objects.all()

    # Apply search filter (case-insensitive)
    if search_query:
        products = products.filter(name__icontains=search_query)

    # Apply category filter, ensuring 'All' shows everything
    if category_filter and category_filter != 'All':
        products = products.filter(category__iexact=category_filter)  # Case-insensitive match

    # Shuffle results using Django's `.order_by('?')` for efficiency
    products = products.order_by('?')

    # Pass data to template
    return render(request, 'marketplace.html', {'products': products})


from django.shortcuts import render, redirect
from inuamkulimaApp.models import Seller
from inuamkulimaApp.forms import SellerForm

def seller_signup(request):
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketplace')
    else:
        form = SellerForm()
    return render(request, 'seller_signup.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import LoanRequestForm

def apply_loan(request):
    if request.method == "POST":
        form = LoanRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect after submission
    else:
        form = LoanRequestForm()

    return render(request, 'loan_application.html', {'form': form})

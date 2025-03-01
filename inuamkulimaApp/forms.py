from django import forms
from .models import ContactMessage
from django import forms
from .models import TrainingSession

from .models import ConsultationRequest


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email address'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject of your message'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your message here...', 'rows': 5}),
        }

        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Your Message',
        }

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = ['course', 'start_date', 'duration', 'location']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'})
        }




from django import forms
from .models import ConsultationRequest
from django import forms
from .models import ConsultationRequest

class ConsultationRequestForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ["name", "email", "phone", "consultation_type", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "phone": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your phone number"}),
            "consultation_type": forms.Select(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 5, "placeholder": "Describe your consultation needs"}),
        }
        labels = {
            "name": "Your Name",
            "email": "Your Email",
            "phone": "Your Phone Number (optional)",
            "consultation_type": "Select Consultation Type",
            "message": "Message (Optional)",
        }

from django import forms
from inuamkulimaApp.models import Seller

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'phone_number', 'email', 'farm_location']

from django import forms
from .models import LoanRequest

from django import forms
from .models import LoanRequest

class LoanRequestForm(forms.ModelForm):
    class Meta:
        model = LoanRequest
        fields = ['name', 'email', 'loan_type', 'amount', 'farm_address', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'loan_type': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Loan amount in Ksh.'}),
            'farm_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter farm location'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe why you need this loan', 'rows': 6}),
        }

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"


class TrainingSession(models.Model):
    course = models.CharField(max_length=200)
    start_date = models.DateField()
    duration = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.course



from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # Ensure MEDIA settings are configured
    category = models.CharField(max_length=50, choices=[
        ('Fruits', 'Fruits'),
        ('Vegetables', 'Vegetables'),
        ('Grains', 'Grains'),
        ('Herbs', 'Herbs'),
        ('Dairy', 'Dairy'),
    ])

    def __str__(self):
        return self.name

from django.db import models
from django.contrib.auth.models import User

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    farm_location = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name






from django.db import models


class ConsultationRequest(models.Model):
    CONSULTATION_TYPES = [
        ("phone", "Phone Consultation"),
        ("video", "Video Call Consultation"),
        ("in-person", "In-person Consultation"),
    ]

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("denied", "Denied"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    consultation_type = models.CharField(max_length=20, choices=CONSULTATION_TYPES)
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    consultation_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.consultation_type} ({self.status})"



from django.db import models

class LoanRequest(models.Model):
    LOAN_TYPES = [
        ('short-term', 'Short-Term Loan'),
        ('long-term', 'Long-Term Loan'),
        ('seasonal', 'Seasonal Loan'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    loan_type = models.CharField(max_length=20, choices=LOAN_TYPES)
    amount = models.PositiveIntegerField()
    farm_address = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.loan_type} ({self.amount} Ksh)"

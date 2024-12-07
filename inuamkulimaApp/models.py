from django.db import models

# Create your models here.
class Member(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.fullname

class Loan(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    LoanType = models.CharField(max_length=200)
    FarmLocation = models.CharField(max_length=50)
    LoanAmount = models.IntegerField()
    message = models.TextField()
    def __str__(self):
        return self.fullname

class Consultation(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    consultation = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name


from django.contrib import admin
from django.urls import path
from inuamkulimaApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('consultation/', views.consultation, name='consultation'),
    path('form/', views.form, name='form'),
    path('contact/', views.contact, name='contact'),
    path('loan/', views.loan, name='loan'),
    path('login/', views.login, name='login'),
    path('market/', views.market, name='market'),
    path('question/', views.question, name='question'),
    path('services/', views.services, name='services'),
    path('weather/', views.weather, name='weather'),
]

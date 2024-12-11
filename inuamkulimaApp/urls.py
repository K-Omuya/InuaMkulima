
from django.contrib import admin
from django.urls import path
from inuamkulimaApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('consultation/', views.consultation, name='consultation'),
    path('', views.form, name='form'),
    path('contact/', views.contact, name='contact'),
    path('loan/', views.loan, name='loan'),
    path('login/', views.login, name='login'),
    path('market/', views.market, name='market'),
    path('question/', views.question, name='question'),
    path('services/', views.service, name='services'),
    path('weather/', views.weather, name='weather'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('show/',views.show,name='show'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('starter/', views.starter, name='starter'),
    path('incentives/', views.incentives, name='incentives'),
    path('trainings/', views.trainings, name='trainings'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
]

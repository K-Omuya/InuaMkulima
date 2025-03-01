from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from inuamkulimaApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/', views.landing, name='landing'),
path("register/", views.user_register, name="user_register"),
    path("login/", views.user_login, name="user_login"),
    # path("logout/", views.user_logout, name="user_logout"),








    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    path('consultation/', views.consultation, name='consultation'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_view, name='contact_success'),
    path('messages/', views.messages_list, name='messages_list'),
    path('delete_message/<int:message_id>/', views.delete_message, name='delete_message'),
    path('loan/', views.loan, name='loan'),
    path('manage/', views.manage, name='manage'),
    path('login/', views.login, name='login'),
    path('market/', views.market, name='market'),
    path('question/', views.question, name='question'),
    path('weather/', views.weather, name='weather'),
    path('show/',views.show,name='show'),
    path('starter/', views.starter, name='starter'),
    path('incentives/', views.incentives, name='incentives'),
    path('trainings/', views.trainings, name='trainings'),
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),

    path('training-sessions/', views.training_sessions, name='training_sessions'),
    path('delete-session/<int:session_id>/', views.delete_session, name='delete_session'),

    path('edit-session/<int:session_id>/', views.edit_training_session, name='edit_training_session'),
    path('request/', views.request_consultation, name='request_consultation'),

    path('marketplace/', views.marketplace, name='marketplace'),

    path('apply-loan/', views.apply_loan, name='apply_loan'),

    path('seller-signup/', views.seller_signup, name='seller_signup'),
    path('manage/', views.manage_consultations, name='manage_consultations'),
    path('approve/<int:request_id>/', views.approve_consultation, name='approve_consultation'),
    path('deny/<int:request_id>/', views.deny_consultation, name='deny_consultation'),
    path("consultation/", views.request_consultation, name="request_consultation"),
    path("consultation-success/", lambda request: render(request, "consultation_success.html"), name="consultation_success"),


]


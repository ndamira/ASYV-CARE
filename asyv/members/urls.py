from django.urls import path
from . import views

urlpatterns = [
    path('clinic_form/', views.clinic_form, name="clinic_form"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('logut_user/', views.logout_user, name="logout_user"),
    path('patients/',views.patients, name="patients"),
    path('history/', views.history, name="history"),
    path('special_meal', views.special_meal, name="special_meal"),
    path('school_regard/', views.school_regard, name="school_regard"),
    path('school_form/', views.school_form, name="school_form"),
    path('school/', views.school, name="school"),
    path('kitchen_form', views.kitchen_form, name="kitchen_form"),
    path('kitchen/', views.kitchen, name="kitchen"),
    path('register_user/', views.register_user, name="register_user"),
    path('school_register_user/', views.school_register_user, name="school_register_user"),
    path('kitchen_register_user/', views.kitchen_register_user, name="kitchen_register_user")
]
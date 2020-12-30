from django.urls import path
from basic_app import views

urlpatterns = [
    path('profile/', views.profile,name="profile"),
    path('other/', views.other,name="other"),
    path('contact/', views.contact,name="contact"),
    path('register/', views.register,name="register")
]
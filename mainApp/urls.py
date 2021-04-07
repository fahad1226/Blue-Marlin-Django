from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('packages/', views.packages, name='packages'),
    path('online-booking/', views.online_booking, name='online_booking'),
    path('contact/', views.contact, name='contact'),
    path('online-booking/store_booking', views.store_booking, name='store_booking'),
    path('contact/store_contact', views.store_contact, name='store_contact'),
]

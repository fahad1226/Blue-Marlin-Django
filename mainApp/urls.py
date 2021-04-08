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

    # sub url of the packages url
    path('packages/venus/', views.venus, name='venus'),
    path('packages/photographer/', views.photographer, name='photographer'),
    path('packages/makeup_artists', views.makeup_artists, name='makeup_artists'),
    path('packages/mehendi_artists/', views.mehendi_artists, name='mehendi_artists'),
    path('packages/bridal_wear/', views.bridal_wear, name='bridal_wear'),
    path('packages/groom_wear/', views.groom_wear, name='groom_wear'),
    path('packages/kazi/', views.kazi, name='kazi'),
    path('packages/decorators/', views.decorators, name='decorators'),
    path('packages/caterers/', views.caterers, name='caterers'),
    path('packages/dj-and-live/', views.dj_and_live, name='dj_and_live'),
    path('packages/invite-card/', views.invite, name='invite'),
    path('packages/other-services/', views.other_services, name='other_services'),
    path('packages/other-services/dhaka/', views.dhaka_services, name='dhaka_service'),
    path('packages/other-services/chittagong/', views.chittagong_services, name='chittagong_service'),
    path('packages/other-services/rajshahi/', views.rajshahi_services, name='rajshahi_service'),
]

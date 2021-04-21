from django.urls import path, include
from .views import ContactFormAPI

urlpatterns = [
    path('api/contact_form', ContactFormAPI.as_view(), name='contact-form'),
]

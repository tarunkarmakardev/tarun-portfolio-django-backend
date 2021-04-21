from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import ContactFormSerializer

from .emails import notify_admin, notify_visitor
# Create your views here.


class ContactFormAPI(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactFormSerializer

    def post(self, request):
        serialzier = ContactFormSerializer(data=request.data)
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        email_address = request.data['email']
        visitor_message = request.data['message']
        if serialzier.is_valid():
            serialzier.save()
            notify_admin(firstname, email_address, visitor_message)
            notify_visitor(firstname, email_address, visitor_message)
            return Response({"Message": 'Response received'}, status=status.HTTP_200_OK)
        return Response(serialzier.errors)

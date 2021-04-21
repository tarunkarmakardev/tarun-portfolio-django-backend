from django.db import models

# Create your models here.

# Contact Form


class Contact(models.Model):
    firstname = models.CharField('First Name', max_length=100)
    lastname = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Email')
    message = models.TextField('Message')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string


def notify_admin(firstname, email, message):
    subject, from_email, to = "Thank you for visiting Tarun Karmakar's portfolio", settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER
    text_content = f"Hello Tarun!, {firstname} just contacted you. They said: {message}. Email: {email} "
    html_message = render_to_string('contact/email_templates/notify_admin_email.html', {
                                    'firstname': firstname, 'message': message, 'email': email})
    send_mail(subject, text_content, from_email,
              [to], html_message=html_message)


def notify_visitor(firstname, email, message):
    subject = "Thank you for visiting Tarun Karmakar's portfolio"
    message = f"Hello {firstname}, your message has been successfully received and I'll get back to you soon."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    html_message = render_to_string(
        'contact/email_templates/thankyou_email.html', {'firstname': firstname})
    send_mail(subject, message, email_from,
              recipient_list, html_message=html_message)

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os

class EmailSend_ResetPassword:
    def __init__(self, data, email, uid, token):
        self.data = data
        self.email = email
        self.uid = uid
        self.token = token

    def mail(self):
        subject = self.data['subject']
        html_content = render_to_string('accounts/reset_email_template.html', {'context' : 'values', 'uid' : self.uid, 'token': self.token})
        plain_content = strip_tags(html_content)
        from_email = os.environ.get('EMAIL_USER')
        to = self.email
        send_mail(subject, plain_content, from_email, [to], html_message=html_content)



class EmailSend_ActivationLink:
    def __init__(self, data, email, token):
        self.data = data
        self.email = email
        self.token = token

    def EmailVerify(self):
        subject = self.data['subject']
        html_content = render_to_string('accounts/email_verify_template.html', {'context' : 'values', 'token': self.token})
        plain_content = strip_tags(html_content)
        from_email = os.environ.get('EMAIL_USER')
        to = self.email
        send_mail(subject, plain_content, from_email, [to], html_message=html_content)
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
        html_content = render_to_string('base/reset_email_template.html', {'context' : 'values', 'uid' : self.uid, 'token': self.token})
        plain_content = strip_tags(html_content)
        from_email = os.environ.get('EMAIL_USER')
        to = self.email
        print(to)
        send_mail(subject, plain_content, from_email, [to], html_message=html_content)
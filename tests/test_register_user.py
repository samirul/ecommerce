import pytest
import uuid
from django.urls import reverse
from BaseID.email import EmailSend_ActivationLink
from account.models import User
from django.contrib.messages import get_messages

@pytest.mark.django_db()
def test_successful_registration(client, registration_user_credentials):
    username, email, password, confirm_password = registration_user_credentials

    response = client.post(reverse('register'),{
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Registration Successful, Please Verify Your Email." in str(message) for message in messages)
    assert response.status_code == 302
    user = User.objects.get(user_name="catty1")
    assert user.user_name == username
    assert user.email == email



@pytest.mark.django_db()
def test_failed_for_invalid_paasword_registration(client, registration_user_credentials):
    username, email, password, confirm_password = registration_user_credentials
    password = "Qx12345"
    confirm_password = "Qx12345"
    response = client.post(reverse('register'),{
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Registration Successful, Please Verify Your Email." not in str(message) for message in messages)
    assert response.status_code == 302
    with pytest.raises(BaseException):
        User.objects.get(user_name="catty1")


@pytest.mark.django_db()
def test_send_email_verification_link_and_verify_link(client, registration_user_credentials):
    username, email, password, confirm_password = registration_user_credentials
    response = client.post(reverse('register'),{
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })
    messages = list(get_messages(response.wsgi_request))
    assert any("Registration Successful, Please Verify Your Email." in str(message) for message in messages)
    assert response.status_code == 302
    email_token_gen = str(uuid.uuid4())
    user = User.objects.get(email=email)
    user.email_token = email_token_gen
    user.save()
    data = {
        'subject' : 'Email Activation Link'
    }
    send_link = EmailSend_ActivationLink(data=data, email=email, token=email_token_gen)
    send_link.EmailVerify()
    assert user.email_token == send_link.token

    response_token = client.get(reverse('verify-email',kwargs={'token': send_link.token}))

    user_token = User.objects.get(email_token=send_link.token)
    user_token.is_active =True
    user.save()
    messages = list(get_messages(response_token.wsgi_request))
    assert any(f"{user.email} - Email Is Successfully Verified." in str(message) for message in messages)
    assert response_token.status_code == 302




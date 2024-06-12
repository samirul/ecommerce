import pytest
from django.urls import reverse
from django.contrib.messages import get_messages


@pytest.mark.django_db()
def test_login_user(client, register_user_for_login_test_pass_for_is_active_true):
    email, password = register_user_for_login_test_pass_for_is_active_true

    response = client.post(reverse("login"),{
        "email": email,
        "password": password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any(f"Login Successful, Welcome Back - {email}" in str(message) for message in messages)
    assert response.status_code == 302



@pytest.mark.django_db()
def test_login_user_fail_for_is_active_false(client, register_user_for_login_test_fail_for_is_active_false):
    email, password = register_user_for_login_test_fail_for_is_active_false

    response = client.post(reverse("login"),{
        "email": email,
        "password": password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any(f"{email} - Email isn't Verified, Please Check Your Email And Verify Your Account First." in str(message) for message in messages)
    assert response.status_code == 302



@pytest.mark.django_db()
def test_login_failed_for_no_email_found_in_the_database(client):
    response = client.post(reverse("login"),{
        "email": "catdog4201@gmail.com",
        "password": "catdog1@!4H"
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("catdog4201@gmail.com - Email isn't Registered, Please Register Your Account First." in str(message) for message in messages)
    assert response.status_code == 302



@pytest.mark.django_db()
def test_login_failed_for_wrong_credentials(client, register_user_for_login_test_pass_for_is_active_true):
    email, _ = register_user_for_login_test_pass_for_is_active_true
    response = client.post(reverse("login"),{
        "email": email,
        "password": "catdog1@!4HKT4v$"
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Invalid Email or Password, Please Check Your Credentials." in str(message) for message in messages)
    assert response.status_code == 302
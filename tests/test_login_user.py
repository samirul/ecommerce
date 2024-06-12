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
def test_login_user_fail(client, register_user_for_login_test_fail_for_is_active_false):
    email, password = register_user_for_login_test_fail_for_is_active_false

    response = client.post(reverse("login"),{
        "email": email,
        "password": password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any(f"{email} - Email isn't Verified, Please Check Your Email And Verify Your Account First." in str(message) for message in messages)
    assert response.status_code == 302
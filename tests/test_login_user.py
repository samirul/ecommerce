import pytest
from django.urls import reverse
from django.contrib.messages import get_messages


@pytest.mark.django_db()
def test_login_user(client, register_user_for_login_test):
    email, password = register_user_for_login_test

    response = client.post(reverse("login"),{
        "email": email,
        "password": password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any(f"Login Successful, Welcome Back - {email}" in str(message) for message in messages)
    assert response.status_code == 302
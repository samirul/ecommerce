import pytest

from django.contrib.messages import get_messages
from django.urls import reverse


@pytest.mark.django_db()
def test_password_doesnt_match(client, password_class_not_match):
    username, email, password, confirm_password = password_class_not_match
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password and Confirm Password Doesn't match." in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_match(client, password_class_match):
    username, email, password, confirm_password = password_class_match
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password and Confirm Password Doesn't match." not in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_not_minimum_8_digit(client, password_class_not_minimum_8_digits):
    username, email, password, confirm_password = password_class_not_minimum_8_digits
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must be minimum 8 characters long." in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_minimum_8_digit(client, password_class_match):
    username, email, password, confirm_password = password_class_match
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must be minimum 8 characters long." not in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_check_upper_class_in_letter(client, password_upper_class_letter):
    username, email, password, confirm_password = password_upper_class_letter
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one uppercase letter." not in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_check_not_upper_class_in_letter(client, password_not_upper_class_letter):
    username, email, password, confirm_password = password_not_upper_class_letter
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one uppercase letter." in str(message) for message in messages)




@pytest.mark.django_db()
def test_password_check_lower_class_in_letter(client, password_lower_class_letter):
    username, email, password, confirm_password = password_lower_class_letter
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one lowercase letter." not in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_check_not_lower_class_in_letter(client, password_not_lower_class_letter):
    username, email, password, confirm_password = password_not_lower_class_letter
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one lowercase letter." in str(message) for message in messages)



@pytest.mark.django_db()
def test_password_check_one_digit(client, password_check_one_digit):
    username, email, password, confirm_password = password_check_one_digit
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one digit." not in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_check_no_digit(client, password_check_not_one_digit):
    username, email, password, confirm_password = password_check_not_one_digit
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one digit." in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_check_one_special_character(client, password_check_one_special_character):
    username, email, password, confirm_password = password_check_one_special_character
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one special character." not in str(message) for message in messages)


@pytest.mark.django_db()
def test_password_check_no_one_special_character(client, password_check_no_special_character):
    username, email, password, confirm_password = password_check_no_special_character
    response = client.post(reverse('register'), {
        "username": username,
        "email": email,
        "password": password,
        "confirmpassword": confirm_password
    })

    messages = list(get_messages(response.wsgi_request))
    assert any("Password must contain at least one special character." in str(message) for message in messages)
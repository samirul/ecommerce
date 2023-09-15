# import pytest
# from django.test import Client
# from django.urls import reverse
# from account.models import User
# from django.contrib.messages import get_messages


# @pytest.fixture
# def client():
#     return Client()

# @pytest.fixture
# def user_data():
#     return {
#         'username': 'sam420',
#         'firstname': 'sam',
#         'lastname': 'haque',
#         'email': 'samirulhaque09@gmail.com',
#         'password': '78945612@Asd',
#         'confirmpassword': '78945612@Asd',
#     }

# @pytest.mark.django_db
# def test_register_view_get(client):
#     url = reverse('register')  
#     response = client.get(url)
#     assert response.status_code == 200
#     assert 'base/register.html' in [template.name for template in response.templates]

# @pytest.mark.django_db
# def test_register_view_post(client, user_data):
#     url = reverse('register')  
#     response = client.post(url, user_data, follow=True)
#     assert response.status_code == 200
#     assert 'base/register.html' in [template.name for template in response.templates]

#     messages = list(get_messages(response.wsgi_request))
#     assert any(message.message == 'Registration Successful, Please Verify Your Email.' for message in messages)

    # assert User.objects.filter(customer_user_name=user_data['username']).exists()
    # assert User.objects.filter(email=user_data['email']).exists()


    

# import pytest
# from account.models import User
# from django.test import Client
# from django.urls import reverse
# from django.contrib.messages.storage.fallback import FallbackStorage

# # @pytest.mark.django_db
# # def test_login_view_get(client):
# #     user = User.objects.create_user(customer_user_name='sam4201',
# #                                     customer_first_name='sam',
# #                                     customer_last_name='haque',
# #                                     email='samirulhaque10@gmail.com')
# #     user.set_password('78945612@Asd')
# #     user.save()
# #     response = client.get(reverse('login'))
# #     assert response.status_code == 200

# @pytest.mark.django_db
# def test_login_view_post_successful(client):
#     user = User.objects.create_user(customer_user_name='sam4201',
#                                     customer_first_name='sam',
#                                     customer_last_name='haque',
#                                     email='samirulhaque10@gmail.com')
#     user.set_password('78945612@Asd')
#     user.save()
#     client = Client()
#     storage = FallbackStorage(client.session)
#     client._session = storage

#     data ={
#         "email" : "samirulhaque10@gmail.com",
#         "password" : "78945612@Asd"
#     }

#     response = client.post(reverse('login'), data=data)

#     assert response.status_code == 200
#     # assert response.url == '/'

#     assert client.session['_auth_user_id'] == str(user.pk)

# # @pytest.mark.django_db
# # def test_login_view_post_invalid_credentials(client):
# #     data ={
# #         "email" : "samirulhaque10@gmail.com",
# #         "password" : "78945612@Asd"
# #     }
# #     response = client.post(reverse('login'), data=data)

# #     assert '_auth_user_id' not in client.session
# #     assert response.status_code == 200
# #     assert b'Invalid Email or Password, Please Check Your Credentials.' in response.content

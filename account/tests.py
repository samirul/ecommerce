from django.test import TestCase
from django.test import Client
from .models import User
from django.urls import reverse



class LoginViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(customer_user_name='sam4201',
                                          customer_first_name='sam',
                                          customer_last_name='haque',
                                          email='samirulhaque10@gmail.com')
        self.user.set_password('78945612@Asd')
        self.user.save()

    def test_register(self):
        data = {
            'username': 'sam420',
            'firstname': 'sam',
            'lastname': 'haque',
            'email': 'samirulhaque09@gmail.com',
            'password': '78945612@Asd',
            'confirmpassword': '78945612@Asd',
            }
        response = self.client.post('/accounts/register/', data=data)
        messages = [msg.message for msg in response.context['messages']]
        print(messages)
        assert "Registration Successful, Please Verify Your Email." in messages

    def test_get_request(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/login.html')

    def test_successful_login(self):
        data = {
            "email" : "samirulhaque10@gmail.com",
            "password" : "78945612@Asd",
        }
        response = self.client.post('/accounts/login/', data=data)
        messages = [msg.message for msg in response.context['messages']]
        expected_message = "Login Successful, Welcome Back - samirulhaque10@gmail.com"
        assert expected_message in messages
        print(messages)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, '/', status_code=302, target_status_code=200)
        # self.assertEqual(response.status_code, 300)

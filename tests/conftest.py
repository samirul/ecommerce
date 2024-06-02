import pytest
from django.test import Client
from account.validators import validate


@pytest.fixture
def client():
    return Client()

#...............................................................
# Testing Password Validator in Register Fixture
#...............................................................

@pytest.fixture
def password_class_not_match():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaAK1"
    confirm_password = "DQtSWaAK1@"
    return username, email, password, confirm_password



@pytest.fixture
def password_class_match():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaAK1@"
    confirm_password = "DQtSWaAK1@"
    return username, email, password, confirm_password



@pytest.fixture
def password_class_not_minimum_8_digits():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSW"
    confirm_password = "DQtSW"
    return username, email, password, confirm_password


@pytest.fixture
def password_upper_class_letter():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaAK1@"
    confirm_password = "DQtSWaAK1@"
    return username, email, password, confirm_password

@pytest.fixture
def password_not_upper_class_letter():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "dqtswaak1@"
    confirm_password = "dqtswaak1@"
    return username, email, password, confirm_password



@pytest.fixture
def password_lower_class_letter():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaAK1@"
    confirm_password = "DQtSWaAK1@"
    return username, email, password, confirm_password

@pytest.fixture
def password_not_lower_class_letter():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQTSWAAK1@"
    confirm_password = "DQTSWAAK1@"
    return username, email, password, confirm_password


@pytest.fixture
def password_check_one_digit():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaAK1@"
    confirm_password = "DQtSWaAK1@"
    return username, email, password, confirm_password

@pytest.fixture
def password_check_not_one_digit():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaAKs@"
    confirm_password = "DQtSWaAKs@"
    return username, email, password, confirm_password



@pytest.fixture
def password_check_one_special_character():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaAK1@"
    confirm_password = "DQtSWaAK1@"
    return username, email, password, confirm_password

@pytest.fixture
def password_check_no_special_character():
    username = 'catty'
    email = 'catty@gmail.com'
    password = "DQtSWaA5Kst"
    confirm_password = "DQtSWaA5Kst"
    return username, email, password, confirm_password


#...............................................................
# Ended Testing Password Validator in Register Fixture
#...............................................................


#...............................................................
#Testing User Registration Fixture
#...............................................................

@pytest.fixture
def registration_user_credentials():
    username = 'catty1'
    email = 'catty1@gmail.com'
    password = "DQtSWaA5Kst@!"
    confirm_password = "DQtSWaA5Kst@!"
    return username, email, password, confirm_password



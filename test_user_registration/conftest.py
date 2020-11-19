import pytest

from user_registration.user_registration import UserRegistration


@pytest.fixture
def instance_of_main_class():
    user_registration =  UserRegistration()
    return user_registration

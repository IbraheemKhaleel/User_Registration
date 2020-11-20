import pytest

from user_registration.input_error import InputError


def test_validate_first_name(instance_of_main_class):
    result = instance_of_main_class.validate_name("Michael")
    assert result.__eq__(True)


def test_invalidate_first_name(instance_of_main_class):
    with pytest.raises(InputError):
        instance_of_main_class.validate_name(" m9 ")


def test_validate_last_name(instance_of_main_class):
    result = instance_of_main_class.validate_name("John")
    assert result.__eq__(True)


def test_invalidate_last_name(instance_of_main_class):
    with pytest.raises(InputError):
        instance_of_main_class.validate_name("b239 ")


def test_validate_phone_number(instance_of_main_class):
    result = instance_of_main_class.validate_phone_number("91 9745945143")
    assert result.__eq__(True)


def test_invalidate_phone_number_should_raise_exception(instance_of_main_class):
    with pytest.raises(InputError):
        instance_of_main_class.validate_phone_number("85875")


@pytest.mark.parametrize("input, expected", [
    ("abc@yahoo.com", True),
    ("abc-100@yahoo.com", True),
    ("abc.100@yahoo.com", True),
    ("abc111@abc.com", True),
    ("abc-100@abc.net", True),
    ("abc.100@abc.com.au", True),
    ("abc@1.com", True),
    ("abc@gmail.com.com", True),
    ("abc+100@gmail.com", True),
    ("abc", False),
    ("abc@.com.my", False),
    ("abc123@.com", False),
    ("abc123@.com.com", False),
    ("abc123@gmail.a", False),
    (".abc@abc.com", False),
    ("abc()*@gmail.com", False),
    ("abc@%*.com", False),
    ("abc..2002@gmail.com", False),
    ("abc.@gmail.com", False),
    ("abc@abc@gmail.com", False),
    ("abc@gmail.com.1a", False),
    ("abc@gmail.com.aa.au", False)
])
def test_validate_email_id(input, expected, instance_of_main_class):
    result = instance_of_main_class.validate_email_id(input)
    assert result == expected

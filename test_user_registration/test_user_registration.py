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

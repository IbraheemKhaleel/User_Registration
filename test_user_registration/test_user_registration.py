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

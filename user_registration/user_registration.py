import re

from user_registration.input_error import InputError


class UserRegistration:
    """
    Created a class for validating user registration
    """
    NAME_PATTERN = r'^[A-Z][A-Za-z]{2,}$'

    def validate_name(self, name):
        """
        :param name:
        :return: if  name matches with pattern, return True
        """
        pattern = re.compile(self.NAME_PATTERN)
        match = pattern.search(name)
        if not match:
            raise InputError(" Enter the first name with minimum three characters ")
        else:
            return True

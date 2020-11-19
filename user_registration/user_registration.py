import re

from user_registration.input_error import InputError


class UserRegistration:
    FIRST_NAME_PATTERN = r'^[A-Z][A-Za-z]{2,}$'

    def validate_first_name(self, first_name):
        """
        :param first_name:
        :return: if first name matches with pattern, return True
        """
        pattern = re.compile(self.FIRST_NAME_PATTERN)
        match = pattern.search(first_name)
        if not match:
            raise InputError("Enter the first name with minimum three characters ")
        else:
            return True

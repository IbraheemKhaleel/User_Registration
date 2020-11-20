import re

from user_registration.input_error import InputError


class UserRegistration:
    """
    Created a class for validating user registration
    """
    NAME_PATTERN = r'^[A-Z][A-Za-z]{2,}$'
    PHONE_NUMBER_PATTERN = r'[9][1][ ][6-9]{1}[0-9]{9}$'
    EMAIL_ID_PATTERN = r'^[A-Za-z0-9]+([-.+_]{1}[0-9A-Za-z]+)*[@][A-Za-z0-9]+[.][a-zA-Z]{2,4}([.,]{1}[a-z]{2,3}){0,1}$'

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

    def validate_phone_number(self, phone_number):
        """
        :param phone_number:
        :return: if  phone number matches with pattern, return True
        """
        pattern = re.compile(self.PHONE_NUMBER_PATTERN)
        match = pattern.search(phone_number)
        if not match:
            raise InputError(" Enter the 10 digit phone number with country code followed by space ")
        else:
            return True

    def validate_email_id(self, email_id):
        """
        :param email_id:
        :return: if email id  matches with pattern, return True
        """
        pattern = re.compile(self.EMAIL_ID_PATTERN)
        match = pattern.search(email_id)
        if not match:
            return False
        else:
            return True



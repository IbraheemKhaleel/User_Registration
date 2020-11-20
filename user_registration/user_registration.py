import re

from user_registration.input_error import InputError


class UserRegistration:
    """
    Created a class for validating user registration
    """
    NAME_PATTERN = r'^[A-Z][A-Za-z]{2,}$'
    PHONE_NUMBER_PATTERN = r'[9][1][ ][6-9]{1}[0-9]{9}$'
    EMAIL_ID_PATTERN = r'^[A-Za-z0-9]+([-.+_]{1}[0-9A-Za-z]+)*[@][A-Za-z0-9]+[.][a-zA-Z]{2,4}([.,]{1}[a-z]{2,3}){0,1}$'
    PASSWORD_PATTERN = r'^(?=.*[A-Z])' + '(?=.*[a-z])' + '(?=.*[!@_#$%^&*])' + '(?=.*[0-9]).{8,}$'

    def pattern_matching(self, input, pattern_input):
        """
        Creating a method for pattern matching
        :param input:
        :param pattern_input:
        :return: matched input
        """
        pattern = re.compile(pattern_input)
        match = pattern.search(input)
        return match

    def validate_name(self, name):
        """
        :param name:
        :return: if  name matches with pattern, return True
        """
        matched_input = self.pattern_matching(name, self.NAME_PATTERN)
        if not matched_input:
            raise InputError(" Enter the first name with minimum three characters ")
        else:
            return True

    def validate_phone_number(self, phone_number):
        """
        :param phone_number:
        :return: if  phone number matches with pattern, return True
        """
        matched_input = self.pattern_matching(phone_number, self.PHONE_NUMBER_PATTERN)
        if not matched_input:
            raise InputError(" Enter the 10 digit phone number with country code followed by space ")
        else:
            return True

    def validate_email_id(self, email_id):
        """
        :param email_id:
        :return: if email id  matches with pattern, return True
        """
        matched_input = self.pattern_matching(email_id, self.EMAIL_ID_PATTERN)
        if not matched_input:
            return False
        else:
            return True

    def validate_password(self, password):
        """
        :param password:
        :return: if password  matches with pattern, return True
        """
        matched_input = self.pattern_matching(password, self.PASSWORD_PATTERN)
        if not matched_input:
            raise InputError('Enter a valid password with one capital letter, special character and a number')
        else:
            return True

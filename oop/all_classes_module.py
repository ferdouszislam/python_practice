from abc import *
import re


class User(ABC):
    """class for all types of signed up users"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, uid=None):
        self.uid = uid

    @abstractmethod
    def validate_credentials(self):
        raise NotImplementedError('abstract method called: validate_credentials()')


class PhoneNumberUser(User):
    """class for users signed up with their phone number"""

    def __init__(self, uid=None, phone_number=None):
        super().__init__(uid)
        self.phone_number = phone_number

    def validate_credentials(self):
        if self.uid is None or self.phone_number is None:
            return False
        return self.__is_valid(self.uid, self.phone_number)

    def __str__(self):
        return 'Credentials: ' + self.phone_number + '[id='+self.uid+']'

    @staticmethod
    def __is_valid(uid, phone_number):
        return len(uid) >= 4 and len(phone_number) == 11 and str.isnumeric(phone_number)


class EmailUser(User):
    """class for users signed up with their email"""

    def __init__(self, uid=None, email=None):
        super().__init__(uid)
        self.email = email

    def validate_credentials(self):
        if self.uid is None or self.email is None:
            return False
        return self.__is_valid(self.uid, self.email)

    def __str__(self):
        return 'Credentials: ' + self.email + '[id='+self.uid+']'

    @staticmethod
    def __is_valid(uid, email):
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        return len(uid) >= 4 and re.search(email_regex, email)

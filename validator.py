import re
from booknary import Booknary

class Validator():

    def __init__(self):
        self

    def make(self, option, argument, message = None):
        validation = self.validate(option, argument)

        if validation:
            return Booknary({'validation' : validation})

        if message == None:
            return Booknary({'validation' : False, 'errors' : self.createMessage(option)})

        return Booknary({'validation' : False, 'errors' : message})

    def validate(self, option, argument):
        return getattr(self, option)(argument)

    def date(self, argument):
        regex = re.match('^\d\d+$', argument)

        if type(regex) is type(None) or len(argument) != 4 or int(argument) < 1900 or int(argument) > 2017:
            return False

        return True

    def email(self, argument):
        regex = re.match('\w+@\w+.com$', argument)

        if type(regex) is type(None) or len(argument) == 0:
            return False

        return True

    def createMessage(self, option):
        if option == 'date':
            return ('A data e invalida')
        if option == 'email':
            return ('O email e invalido')

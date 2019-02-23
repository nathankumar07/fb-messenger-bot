

class Check:

    def __init__(self, user_name = None, recipient_email = None, check_amount = None):
        pass

    def set_user_name(name):
        self.user_name = name

    def set_recipient_email(email):
        self.recipient_email = email

    def set_check_amount(amount):
        self.check_amount = amount

    def is_Complete_Check():
        if (self.user_name != None and self.recipient_email != None and self.check_amount != None):
            return True
        else:
            return False

    def get_user_name():
        return self.user_name

    def get_recipient_email():
        return self.recipient_email

    def get_check_amount():
        return self.check_amount

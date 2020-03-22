class Account:
    def __init__(self, account):
        self.data = str(account).strip()
        self.isdigit()
        # number of digits of the account
        self.digits_count = len(self.data)

    def isdigit(self):
        """
        check if any non-digit char in account
        """
        if not self.data.isdigit():
            raise ValueError('Account can contain digits only')

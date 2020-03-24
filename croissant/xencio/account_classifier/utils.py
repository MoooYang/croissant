class Account:
    def __init__(self, account):
        self.data = str(account).strip()
        # number of digits of the account
        self.digits_count = len(self.data)
        self.isdigit()
        self.valid_len()

    def isdigit(self):
        """
        check if any non-digit char in account
        """
        if not self.data.isdigit():
            raise ValueError('Error: account contain non-digits')

    def valid_len(self):
        if not 9 <= self.digits_count <= 21:
            raise ValueError('Error: set a value of between 9 and 21 characters')


class ResultContainer:
    def __init__(self, account, bank):
        self.flag = 0
        self.account = account
        self.attributes = dict()

        self.bank_alias = {'icbc': '工商银行', 'ccb': '建设银行', 'boc': '中国银行',
                           'abc': '农业银行', 'bcm': '交通银行', 'psbc': '邮储银行',
                           'cib': '兴业银行', 'cgb': '广发银行', 'cmsb': '民生银行',
                           'cmbc': '招商银行', 'ceb': '光大银行', 'spdb': '浦发银行',
                           'citic': '中信银行'}
        self.bank = self.bank_alias[bank]

    def evaluate(self):
        """
        May upgrade to rating system later on
        :return:
        """
        for attribute in self.attributes.values():
            self.flag += attribute['weight']

        return self.flag

    def attributes_append(self, title, contain, weight):
        attribute = {'contain': contain, 'weight': weight}
        self.attributes[title] = attribute

    def __str__(self):
        output = [f'Bank:{self.bank}']
        for title, attribute in self.attributes.items():
            output.append(f"{title}:{attribute['contain']}")
        return ",".join(output)

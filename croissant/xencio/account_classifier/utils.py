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


class ResultContainer:
    def __init__(self, account, bank):
        self.flag = False
        self.account = account
        self.attributes = dict()

        self.bank_alias = {'icbc': '工商银行', 'ccb': '建设银行', 'boc': '中国银行',
                           'abc': '农业银行', 'bcm': '交通银行', 'psbc': '邮储银行',
                           'cib': '兴业银行', 'cgb': '广发银行', 'cmsb': '民生银行',
                           'cmbc': '招商银行', 'ceb': '光大银行', 'spdb': '浦发银行',
                           'citic': '中信银行'}
        self.bank = self.bank_alias[bank]

    def majority_vote(self):
        true, false = 0, 0
        for attribute in self.attributes.values():
            if attribute['flag']:
                true += 1
            else:
                false += 1
        self.flag = true > false
        return self.flag

    def attributes_append(self, title, contain, flag):
        attribute = {'contain': contain, 'flag': flag}
        self.attributes[title] = attribute

    def __str__(self):
        output = [f'Bank:{self.bank}']
        for title, attribute in self.attributes.items():
            output.append(f"{title}:{attribute['contain']}")
        return ",".join(output)

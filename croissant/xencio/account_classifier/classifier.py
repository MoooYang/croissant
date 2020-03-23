from .account import Account
from .bank import Bank


class AccountClassifier:
    def __init__(self):
        # temperately store Account object
        self.account = None
        self.results = []
        self.bank_alias = {'icbc': '工商银行', 'ccb': '建设银行', 'boc': '中国银行',
                           'abc': '农业银行', 'bcm': '交通银行', 'psbc': '邮储银行',
                           'cib': '兴业银行', 'cgb': '广发银行', 'cmsb': '民生银行',
                           'cmbc': '招商银行', 'ceb': '光大银行', 'spdb': '浦发银行',
                           'citic': '中信银行'}

        self.digits_count_map = {9: ['cmsb'],
                                 12: ['boc'],
                                 15: ['cmbc'],
                                 16: ['cmsb'],
                                 17: ['abc', 'ceb'],
                                 18: ['cib', 'cgb', 'psbc'],
                                 19: ['citic', 'cgb', 'icbc'],
                                 20: ['ccb', 'spdb'],
                                 21: ['bcm']
                                 }

    def check(self, account):
        try:
            self.account = Account(account)
        except ValueError as E:
            print(E)
            return

        self._get_bank()
        return self._parse_result()

    def _get_bank_candidates(self):
        """
        Get possible bank based on number of digits of the account
        :return: list of bank_name(str) or None
        """
        return self.digits_count_map.get(self.account.digits_count, None)

    def _get_bank(self):
        """
        check each bank in candidate banks
        """
        bank_candidates = self._get_bank_candidates()
        if bank_candidates:
            for bank_name in bank_candidates:
                bank = Bank(bank_name, self.account.digits_count)
                result = bank.check(self.account)
                if result[0][0]:
                    # Store the results in self.results temporarily
                    self.results.append((bank_name, result))

    def _parse_result(self):
        results_list = []
        # There might be multiple banks
        for result in self.results:
            result_dict = {}

            """Unwrap result"""
            bank_name, check_result = result
            other_result, location_result = check_result

            """Format output"""
            result_dict['Bank'] = self.bank_alias[bank_name]
            result_dict['Location'] = location_result
            for key, value in other_result[1]:
                result_dict[key] = value

            results_list.append(result_dict)
        # clear self.result cache
        self.results = []

        return results_list if results_list else 'Unknown'


if __name__ == "__main__":
    classifier = AccountClassifier()
    accounts = ['0200003509000203564',
                '1702020709200046017',
                '3301009209200064313',
                '0302099619100088778',
                '0200316809100022565',
                '0302096809100013142',
                '0408020009300125789']
    for acc in accounts:
        print(classifier.check(acc))

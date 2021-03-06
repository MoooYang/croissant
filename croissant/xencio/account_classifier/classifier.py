from .utils import Account
from .bank import Bank


class AccountClassifier:
    def __init__(self):
        # temperately store Account object
        self.account = None
        self.results = []

        self.digits_count_map = {9: [('cmsb', True)],
                                 12: [('boc', True)],
                                 15: [('cmbc',)],
                                 16: [('cmsb',)],
                                 17: [('abc',), ('ceb',), ("spdb",)],
                                 18: [('cib',), ('cgb',), ('psbc',)],
                                 19: [('citic',), ('cgb',), ('icbc',)],
                                 20: [('ccb',), ('spdb',)],
                                 21: [('bcm',)]
                                 }

    def check(self, account):
        try:
            self.account = Account(account)
        except ValueError as E:
            raise E
        results = self._check_bank_candidates()
        if results:
            return max(results, key=lambda result: result.flag)

    def _check_bank_candidates(self):
        """
        check each bank in candidate banks
        """
        results = list()
        bank_candidates = self._get_bank_candidates()
        if bank_candidates:
            for bank_name, *isRandom in bank_candidates:
                bank = Bank(bank_name, self.account.digits_count, isRandom)
                result = bank.check(self.account)
                if result.evaluate():
                    # Store the results in self.results temporarily
                    results.append(result)
        return results

    def _get_bank_candidates(self):
        """
        Get possible bank based on number of digits of the account
        :return: list of bank_name(str) or None
        """
        return self.digits_count_map.get(self.account.digits_count, None)


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

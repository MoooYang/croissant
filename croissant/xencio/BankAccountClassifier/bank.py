from .account import Account


class Bank:
    def __init__(self, name, digits):

        """Bank specify feature"""
        # list of int
        self.digits_counts = digits
        # list of tuple (tag, start, end, list(str)
        self.fix_combinations_path = "./static/" + name + '_' + str(digits) + '_' + "fix_combinations"
        # path of file which contain location information
        self.location_map_path = "./static/" + name + '_' + str(digits) + '_' + "location_map"

        """class feature"""
        # Temporarily store account object
        self.account = None
        # Position of digits in account which indicate the location of bank
        self.location_position = ()
        self.location_map = {}
        self.fix_combinations = []
        # list of check results
        self.votes = []

    def check(self, account):
        """
        Check weather belongs to the bank, if yes than match location
        :type account: Account
        :return: (Boolean, List(Tuple(tag, Boolean),location)
        """
        self.account = account
        parse_result = self._parse()
        if parse_result[0]:
            return parse_result, self._get_location()
        return parse_result, 'Unknown'

    def _parse(self):
        """
        check whether this account belongs to this bank
        :return: (Boolean, List(Tuple(tag, Boolean))
        """
        # reinitialise votes
        self.votes = []
        self._check_digits_count()
        self._check_fix_combinations()
        return self.majority_vote()

    def _check_fix_combinations(self):
        if not self.fix_combinations:
            self._read_fix_combinations()
        for combination in self.fix_combinations:
            """Unwrap combination"""
            tag, start, end, candidates = combination
            self.votes.append((tag,
                               self.account.data[start:end]
                               if self.account.data[start:end] in candidates else False))

    def _check_digits_count(self):
        self.votes.append(('Digits count',
                           self.digits_counts
                           if self.account.digits_count == self.digits_counts else False))

    def majority_vote(self):
        true = 0
        false = 0
        for tag, vote in self.votes:
            if vote:
                true += 1
            else:
                false += 1
        return true >= false, self.votes

    def _get_location(self):
        if not self.location_map:
            self._read_location_map()
            start, end = self.location_position[0], self.location_position[1]
        return self.location_map.get(self.account.data[start:end],
                                     'Unknown')

    def _read_location_map(self):
        with open(self.location_map_path, 'r') as file:
            line = file.readline().strip().split(',')
            self.location_position = (int(line[0]), int(line[1])+1)
            for line in file.readlines():
                line = line.strip().split(',')
                self.location_map[line[0]] = line[1]

    def _read_fix_combinations(self):
        with open(self.fix_combinations_path, 'r') as file:
            for line in file.readlines():
                line = line.strip().split(',')
                tag, start, end, candidates = line[0], int(line[1]), int(line[2])+1, line[3:]
                self.fix_combinations.append((tag, start, end, candidates))


if __name__ == "__main__":
    icbc = Bank('icbc', 19)
    accounts = ['0200003509000203564',
                '1702020709200046017',
                '3301009209200064313',
                '0302099619100088778',
                '0200316809100022565',
                '0302096809100013142',
                '0408020009300125789']
    for a in accounts:
        acc = Account(a)
        print(icbc.check(acc))

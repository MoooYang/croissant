from .utils import Account, ResultContainer
from os.path import exists


class Bank:
    def __init__(self, name, digits, random=False):

        """Bank specify feature"""
        self.name = name
        # Indicate whether there are rules apply to accounts
        self.random = random
        # list of int
        self.digits_counts = digits
        # list of tuple (tag, start, end, list(str)
        self.fix_combinations_path = "./xencio/account_classifier/static/" + name + '_' + str(
            digits) + '_' + "fix_combinations"
        # path of file which contain location information
        self.location_map_path = "./xencio/account_classifier/static/" + name + '_' + str(digits) + '_' + "location_map"

        """class feature"""
        # Temporarily store account object
        self.account = None
        # Position of digits in account which indicate the location of bank
        self.location_position = ()
        self.location_map = {}
        self.fix_combinations = []
        self.result = None

    def check(self, account):
        """
        Check weather belongs to the bank, if yes than match location
        :type account: Account
        :return: (Boolean, List(Tuple(tag, Boolean),location)
        """
        self.account = account
        # reinitialise self.result
        self.result = ResultContainer(account, self.name)
        # if the bank random assign each account
        self._check_location()
        self._check_digits_count()
        self._check_fix_combinations()
        if self.random:
            self.result.attributes_append('Randomness', 'True', 1)

        return self.result

    def _check_fix_combinations(self):
        self._read_fix_combinations()
        for combination in self.fix_combinations:
            """Unwrap combination"""
            tag, start, end, candidates_dict = combination
            self.result.attributes_append(tag,
                                          candidates_dict.get(self.account.data[start:end], 'Unknown'),
                                          1 if self.account.data[start:end] in candidates_dict else 0
                                          )

    def _check_digits_count(self):
        self.result.attributes_append('Digits Count',
                                      self.digits_counts,
                                      0)

    def _check_location(self):
        self._read_location_map()

        if self.location_position:
            start, end = self.location_position[0], self.location_position[1]
            code = self.account.data[start:end]
            self.result.attributes_append('Location',
                                          self.location_map.get(code, 'Unknown'),
                                          1 if code in self.location_map else 0
                                          )
        else:
            self.result.attributes_append('Location', 'No Data', 0)

    def _read_location_map(self):
        # when file exists and have not read before
        if exists(self.location_map_path) and not self.location_position:
            with open(self.location_map_path, 'r') as file:
                line = file.readline().strip().split(',')
                self.location_position = (int(line[0]), int(line[1]) + 1)
                for line in file.readlines():
                    line = line.strip().split(',')
                    self.location_map[line[0]] = line[1]

    def _read_fix_combinations(self):
        # when file exists and have not read before
        if exists(self.fix_combinations_path) and not self.fix_combinations:
            with open(self.fix_combinations_path, 'r') as file:
                for line in file.readlines():
                    line = line.strip().split(',')
                    tag, start, end, candidates_list = line[0], int(line[1]), int(line[2]) + 1, line[3:]
                    candidates_dict = dict()
                    for candidate in candidates_list:
                        key, *value = candidate.split('-')
                        candidates_dict[key] = value[0] if value else key
                    self.fix_combinations.append((tag, start, end, candidates_dict))


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

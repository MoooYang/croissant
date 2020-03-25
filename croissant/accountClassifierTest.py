from xencio.account_classifier.classifier import AccountClassifier
from collections import defaultdict
import requests

if __name__ == "__main__":
    classifier = AccountClassifier()

    banks = {'工商银行', '建设银行', '中国银行',
             '农业银行', '交通银行', '邮储银行',
             '兴业银行', '广发银行', '民生银行',
             '招商银行', '光大银行', '浦发银行',
             '中信银行'}
    total_dict = defaultdict(int)
    right_dict = defaultdict(int)
    total = 0
    right = 0
    error = 0
    with open('account_data', 'r') as file:
        for line in file.readlines():
            mylist = line.strip().split()
            try:
                if mylist[1] in banks:
                    # result = classifier.check(mylist[0])
                    # result=requests.get("http://ymo.wiki/xencio/account/"+mylist[0])
                    total += 1
                    total_dict[mylist[1]] += 1
                    if result.bank == mylist[1]:
                        right += 1
                        right_dict[result.bank] += 1
            except Exception as E:
                print(E)
                error += 1
    print('Error: ', error)
    print(total_dict)
    print(right_dict)
    print(total)
    print(right)

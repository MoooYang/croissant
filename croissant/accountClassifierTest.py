from xencio.account_classifier.classifier import AccountClassifier

if __name__ == "__main__":
    classifier = AccountClassifier()
    accounts = ['91060155400000093',
               ]
    for acc in accounts:
        print(classifier.check(acc))
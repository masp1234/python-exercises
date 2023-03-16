class Bank:
    def __init__(self, name, accounts=[]):
        self.name = name
        self.accounts = accounts

    def add_account(self, *accounts):
        for account in accounts:
            self.accounts.append(account)
    
    def __str__(self):
        return f'{self.name}, accounts: {self.accounts}'


class Account:
    def __init__(self, account_number, account_type='Checking'):
        self.account_number = account_number
        self.account_type = account_type
    def __str__(self):
        return f'Account number: {self.account_number}, account type: {self.account_type}'


class Customer:
    def __init__(self, social_security_number, name, age):
        self.social_security_number = social_security_number
        self.name = name
        self.age = age



# Underligt at accounts ikke bruger __str__ når print(bank) bliver kaldt. Hvis man printer dem for sig selv, bliver __str__ brugt

checking_account = Account('NUMBER')
print(checking_account)

investing_account = Account('1212ACCOUNTNUMBER', 'Investing')
print(investing_account)

danske_bank = Bank('Danske Bank')
print(danske_bank)


danske_bank.add_account(investing_account, checking_account)
print(danske_bank)
print(danske_bank.accounts[0], danske_bank.accounts[1])

accounts = [checking_account, investing_account]

jyske_bank = Bank('Jyske Bank', accounts)
print(jyske_bank)



        
import random
import string

class Account():
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)
        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, 'value'):
            self.value = 0
        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank():
    @staticmethod
    def isAccValid(account):
        if not isinstance(account, Account):
            return False
        dicted = account.__dict__
        if len(dicted.keys()) % 2 == 0:
            return False
        if len([a for a in dicted.keys() if a.startswith('b')]) > 0:
            return False
        if len([a for a in dicted.keys() if a.startswith('addr')]) == 0:
            return False
        if len([a for a in dicted.keys() if a.startswith('zip')]) == 0:
            return False
        if not "name" in dicted.keys() or\
                not "id" in dicted.keys() or\
                not "value" in dicted.keys():
            return False
        if not isinstance(account.name, str):
            return False
        if not isinstance(account.id, int):
            return False
        if not isinstance(account.value, (int, float)):
            return False
        return True

    def __init__(self):
        self.accounts = []

    def add(self, account):
        if isinstance(account, Account):
            for acc in self.accounts:
                if acc.id == account.id:
                    print("Account already exist")
                    return False
            self.accounts.append(account)
        else:
            print("Account addition error")
            return False


    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin: str(name) of the first account
            @dest: str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return True if success, False if an error occured
        """
        origAcc = None
        destAcc = None

        for acc in self.accounts:
            if acc.name == origin:
                origAcc = acc
            elif acc.name == dest:
                destAcc = acc
        if not origAcc or not destAcc or \
                not self.isAccValid(origAcc) or \
                not self.isAccValid(destAcc) or \
                not isinstance(amount, (int, float)) or \
                origAcc.value < amount:
            return False
        origAcc.value -= amount
        destAcc.value += amount
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        if not isinstance(name, str):
            return False
        account = None
        for acc in self.accounts:
            if acc.name == name:
                account = acc
        if not account:
            print("fix Failed")
            return False
        arr = [a for a in account.__dict__.keys() if a.startswith('b')]
        for key in arr:
            account.__dict__.pop(key)
        if len([a for a in account.__dict__.keys() if a.startswith('addr')]) == 0:
            account.addr = "42 rue Default"
        if len([a for a in account.__dict__.keys() if a.startswith('zip')]) == 0:
            account.zip = "00000"
        if not "id" in account.__dict__.keys():
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not "value" in account.__dict__.keys():
            account.value = 0
        if not isinstance(account.id, int):
            account.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not isinstance(account.value, (int, float)):
            account.value = 0
        if len(account.__dict__.keys()) % 2 == 0:
            newAttr = "b"
            letters = string.ascii_lowercase
            while newAttr.startswith("b") or newAttr in account.__dict__.keys():
                newAttr = ''.join(random.choice(letters) for i in range(8))
            account.__dict__[newAttr] = newAttr
        return True
        

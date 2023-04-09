import random
import string

from termcolor import cprint

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

    def fix(self):
        arr = [a for a in self.__dict__.keys() if a.startswith('b')]
        for key in arr:
            self.__dict__.pop(key)
        if len([a for a in self.__dict__.keys() if a.startswith('zip') or a.startswith('addr')]) == 0:
            self.zip = "00000"
        if not "id" in self.__dict__.keys():
            self.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not "value" in self.__dict__.keys():
            self.value = 0
        if not isinstance(self.id, int):
            self.id = Account.ID_COUNT
            Account.ID_COUNT += 1
        if not isinstance(self.value, (int, float)):
            self.value = 0
        if len(self.__dict__.keys()) % 2 == 0:
            newAttr = "b"
            letters = string.ascii_lowercase
            while newAttr.startswith("b") or newAttr in self.__dict__.keys():
                newAttr = ''.join(random.choice(letters) for i in range(8))
            self.__dict__[newAttr] = newAttr
        return self


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
        if len([a for a in dicted.keys() if a.startswith('addr') or a.startswith('zip')]) == 0:
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
        origAcc.transfer(-amount)
        destAcc.transfer(amount)
        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        account = None
        if isinstance(name, str):
            for acc in self.accounts:
                if acc.name == name:
                    account = acc
            if not account:
                return False
            account.fix()
            return True
        if isinstance(name, Account):
            account = name
            return account.fix()
        print("fix Failed")
        return False


if __name__ == "__main__":
    cprint("### # 01.05.01", "green")
    
    bank = Bank()
    john = Account(
        'William John',
        zip='100-064',
        brother="heyhey",
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol = "hihi"
    )
    print(bank.fix_account(john))
    bank.fix_account('William John')

    cprint("### # 01.05.02", "green")
    john = Account(
        'William John',
        zip='100-064',
        rother="heyhey",
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
    )
    print("isValid:", Bank.isAccValid(john))
    cprint("### # 01.05.03", "green")
    john = Account(
        'William John',
        zip='100-064',
        rother="heyhey",
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None,
        other='This is the vice president of the corporation',
        lol = "lolilol"
    )
    print("isValid:", Bank.isAccValid(john))

    cprint("### # 01.05.04", "green")
    bank.add(
        Account(
            'Jane',
            zip='911-745',
            value=1000.0,
            ref='1044618427ff2782f0bbece0abd05f31'
        )
    )

    jhon = Account(
        'Jhon',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    )

    bank.add(jhon)

    print("testing a valid transfer")
    print(jhon.value)
    print(bank.transfer("Jane", "Jhon", 500))
    print(jhon.value)
    cprint("### # 01.05.05", "green")
    print(bank.transfer("Jane", "Jhon", 1000))
    print(jhon.value)

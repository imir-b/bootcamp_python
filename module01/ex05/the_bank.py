class Account(object):

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

class Bank(object):
    """The bank"""

    def __init__(self):
        self.accounts = []

    def add(self, new_account):
        """ Add new_account in the Bank
        @new_account: Account() new account to append
        @return True if success, False if an error occured
        """
        # test if new_account is an Account() instance and if
        # it can be appended to the attribute accounts
        # ... Your code ...
        try :
            if not isinstance(new_account, Account):
                raise TypeError("new_account must be an instance of Account.")
            self.accounts.append(new_account)
            return True
        except Exception as e:
            print(f"Error adding account: {e}")
            return False

    def transfer(self, origin, dest, amount):
        """" Perform the fund transfer
        @origin: str(name) of the first account
        @dest: str(name) of the destination account
        @amount: float(amount) amount to transfer
        @return True if success, False if an error occured
        """
        # ... Your code ...
        if not isinstance(origin, str) or not (isinstance(dest, str)):
            print("Error: origin and dest must be strings.")
            return False

        if not isinstance(amount, (int, float)) or amount < 0:
            print("Error: amount must be a non-negative number.")
            return False

        if origin == dest:
            print("Error: origin and dest cannot be the same.")
            return False
        
        if not any(acc.name == origin for acc in self.accounts):
            print(f"Error: origin account '{origin}' does not exist.")
            return False

        if not any(acc.name == dest for acc in self.accounts):
            print(f"Error: destination account '{dest}' does not exist.")
            return False

        if not any(acc.name == origin and acc.value >= amount for acc in self.accounts):
            print(f"Error: insufficient funds in origin account '{origin}'.")
            return False
        
        if not origin == dest:
            origin_account = next(acc for acc in self.accounts if acc.name == origin)
            dest_account = next(acc for acc in self.accounts if acc.name == dest)
            origin_account.transfer(-amount)
            dest_account.transfer(amount)
        return True
        
# How do we define if a bank account is corrupted? A corrupted bank account has:
# • an even number of attributes,
# • an attribute starting with b,
# • no attribute starting with zip or addr,
# • no attribute name, id and value,
# • name not being a string,
# • id not being an int,
# • value not being an int or a float

    def is_account_corrupted(self, account):
        """ Check if an account is corrupted"""
        if not isinstance(account, Account):
            print("Error: account must be an instance of Account.")
            return True

        attributes = account.__dict__.keys()

        if len(attributes) % 2 == 0:
            return True

        if any(attr.startswith('b') for attr in attributes):
            return True

        if not any(attr.startswith('zip') for attr in attributes) and not any(attr.startswith('addr') for attr in attributes):
            return True

        if not hasattr(account, 'name') or not isinstance(account.name, str):
            return True

        if not hasattr(account, 'id') or not isinstance(account.id, int):
            return True

        if not hasattr(account, 'value') or not isinstance(account.value, (int, float)):
            return True

        return False

    def fix_account(self, name):
        """ fix account associated to name if corrupted
        @name: str(name) of the account
        @return True if success, False if an error occured
        """
        # ... Your code ...
        account = next((acc for acc in self.accounts if acc.name == name), None)
        if account is None:
            print(f"Error: account '{name}' does not exist.")
            return False
        
        if self.is_account_corrupted(account):

            if not hasattr(account, 'name'):
                account.name = name
            if not hasattr(account, 'id'):
                account.id = Account.ID_COUNT
                Account.ID_COUNT += 1
            if not hasattr(account, 'value'):
                account.value = 0

            if not any(attr.startswith('zip') for attr in account.__dict__):
                account.zip = ''
            if not any(attr.startswith('addr') for attr in account.__dict__):
                account.addr = ''

            for attr in list(account.__dict__.keys()):
                if attr.startswith('b'):
                    delattr(account, attr)

            if len(account.__dict__) % 2 == 0:
                account.extra_attr = None

        return True

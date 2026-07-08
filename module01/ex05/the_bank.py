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
    
if __name__ == "__main__":
    print("=== 1. INITIALISATION DE LA BANQUE ===")
    bank = Bank()
    print("Banque créée avec succès.\n")

    print("=== 2. CRÉATION DE COMPTES ===")
    # Comptes valides
    acc_john = Account("John", value=100.0, zip='75000', addr='Paris')
    acc_jane = Account("Jane", value=50.0, zip='69000', addr='Lyon')
    print(f"Compte 1: {acc_john.name}, Solde: {acc_john.value}, ID: {acc_john.id}")
    print(f"Compte 2: {acc_jane.name}, Solde: {acc_jane.value}, ID: {acc_jane.id}")
    
    # Compte invalide (doit lever une erreur)
    try:
        acc_invalid = Account("Invalid", value=-50)
    except AttributeError as e:
        print(f"Test compte négatif réussi (Erreur interceptée) : {e}")

    print("\n=== 3. AJOUT DES COMPTES À LA BANQUE ===")
    bank.add(acc_john)
    bank.add(acc_jane)
    print("Ajout de John et Jane réussi.")
    
    # Test d'ajout invalide
    print("Tentative d'ajout d'une chaîne de caractères :")
    bank.add("Ceci n'est pas un compte") 

    print("\n=== 4. TESTS DE TRANSFERTS VALIDES ===")
    print(f"Avant transfert - John: {acc_john.value} | Jane: {acc_jane.value}")
    success = bank.transfer("John", "Jane", 20.0)
    print(f"Transfert (John -> Jane, 20.0) réussi ? {success}")
    print(f"Après transfert - John: {acc_john.value} (attendu 80.0) | Jane: {acc_jane.value} (attendu 70.0)")

    print("\n=== 5. TESTS DE TRANSFERTS INVALIDES ===")
    print("-> Test: Fonds insuffisants")
    bank.transfer("John", "Jane", 1000.0)
    
    print("-> Test: Compte inexistant")
    bank.transfer("John", "Ghost", 10.0)
    
    print("-> Test: Transfert vers soi-même")
    bank.transfer("John", "John", 10.0)
    
    print("-> Test: Montant négatif")
    bank.transfer("John", "Jane", -10.0)

    print("\n=== 6. TEST DE CORRUPTION ET RÉPARATION ===")
    # On crée un compte volontairement "corrompu" en manipulant son dictionnaire
    acc_corrupt = Account("Corrupt", value=10.0)
    acc_corrupt.bad_attribute = "Je ne devrais pas être là" # Commence par 'b'
    del acc_corrupt.value # On supprime la valeur
    bank.add(acc_corrupt)
    
    print(f"Attributs du compte corrompu avant réparation : {acc_corrupt.__dict__.keys()}")
    
    # Note : Cela va planter si tu n'as pas implémenté `is_account_corrupted` !
    try:
        bank.fix_account("Corrupt")
        print(f"Attributs du compte après réparation : {acc_corrupt.__dict__.keys()}")
        print(f"Valeur restaurée : {acc_corrupt.value}")
    except AttributeError as e:
        print(f"❌ ERREUR: La réparation a planté. As-tu oublié de coder `is_account_corrupted` ? Détail : {e}")
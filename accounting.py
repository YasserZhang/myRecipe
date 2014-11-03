#basic class or super class Account in which methods necessary for creating an account, and debiting
# and crediting money are set up
class Account(object):
    def __init__(self,name):
        self.name = name
        self.debit = [0]
        self.credit = [0]
        self.description = {}
        self.is_debit = None
    def __str__(self):
        return self.name
    def debit(self,value):
        self.debit.append(value)
    def credit(self,value):
        self.credit.append(value)
    def get_debit(self):
        return self.debit[-1]
    def get_credit(self):
        return self.credit[-1]


# subclass Permanent and Temporary

# create Permanent accounts under Perm
class Perm(Account):
    def is_permanent(self):
        return True

class Asset(Perm):
    def __init__(self,name):
        Account.__init__(self,name)
        self.is_debit = True
    def get_balance(self):
        return sum(self.debit) - sum(self.credit)

class Current_Asset(Asset):
    def is_current(self):
        return True
class Non_C_Asset(Asset):
    def is_current(self):
        return False
    
    
    
class Liability(Perm):
    def __init__(self,name):
        Account.__init__(self,name)
        self.is_debit = False
    def get_balance(self):
        return sum(self.credit) - sum(self.debit)
class Equity(Perm):
    def __init__(self,name):
        Account.__init__(self,name)
        self.is_debit = False
    def get_balance(self):
        return sum(self.credit) - sum(self.debit)

class XAsset(Perm):
    def __init__(self,name):
        Account.__init__(self,name)
        self.is_debit = False
    def get_balance(self):
        return sum(self.credit) - sum(self.debit)    
# create all temporary accounts under Temp     
class Temp(Account):
    def is_permanent(self):
        return False
# under Temp class exist two subclasses: Revenue and Expense
class Revenue(Temp):
    # Revenue account which is credit account
    def get_balance(self):
        return sum(self.credit) - sum(self.debit)

class Expense(Temp):
    # Expense account which is debit account
    def get_balance(self):
        return sum(self.debit - self.credit)
    def set_SGA(self, boo=False):
        self.is_SGA = boo
    def is_SGA(self):
        return self.is_SGA
    
    
cash = Perm("Cash")
print cash

## debit and credit are methods for journal entries

# get the total balance of the account based on if it is debit or credit account
# if debit, then sum of debit - sum of credit
# if credit, then sum of credit - sum of debit
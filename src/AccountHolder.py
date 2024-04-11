class AccountHolder:
  def __init__(self, balance, firstName, lastName, accountID):
    self.balance = balance
    self.firstName = firstName
    self.lastName = lastName
    self.accountID = accountID

  def getBalance(self):
    return self.balance

  def getFirstName(self):
    return self.firstName

  def getLastName(self):
    return self.lastName

  def getAccountID(self):
    return self.accountID

  def setBalance(self, newBalance):
    self.balance = newBalance

  def setFirstName(self, newFirstName):
    self.firstName = newFirstName

  def setLastName(self, newLastName):
    self.lastName = newLastName

  def withdraw(self, moneyToWithdraw):
    if (moneyToWithdraw > self.balance):
      print("Not enough funds")
    else:
      self.setBalance(self.balance - moneyToWithdraw)
    return self.balance

  def deposit(self, moneyToDeposit):
    self.setBalance(self.balance + moneyToDeposit)
    return self.balance

  def __str__(self):
    # just re-learning how to do toString but in Python, we 
    # don't need to keep this at all
    return self.firstName + " " + self.lastName
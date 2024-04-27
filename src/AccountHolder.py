'''
Brandon Pranke
Melissa Brown

CSC 330 Language Design and Implementation

4/28/2024

Week 7: Final Project

Creates an Account Holder class which will be used with our Banking language to create accounts and withdraw 
or deposit money

We certify that this is our own original work

'''

class AccountHolder:
  def __init__(self, balance, firstName, lastName, accountID):
    self.balance = balance
    self.firstName = firstName
    self.lastName = lastName
    self.accountID = accountID

# Lines 26 - 44 are getters / setters for attributes
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

  # Subtracts balance from account holder object and returns new balance
  # If account does not have sufficient funds, a message will be printed to the user
  # to alert them that they are not wealthy enough. In this case, the original
  # balance is returned
  def withdraw(self, moneyToWithdraw):
    if (moneyToWithdraw > self.balance):
      print("Not enough funds")
    else:
      self.setBalance(self.balance - moneyToWithdraw)
    return self.balance

  # Adds balance to account holder object and returns new balance
  def deposit(self, moneyToDeposit):
    self.setBalance(self.balance + moneyToDeposit)
    return self.balance

  # In a print statement, account holder first and last name is printed
  def __str__(self):
    return self.firstName + " " + self.lastName
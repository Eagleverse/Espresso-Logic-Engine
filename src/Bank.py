'''
Brandon Pranke
Melissa Brown

CSC 330 Language Design and Implementation

4/28/2024

Week 7: Final Project

Creates a Bank class which holds a mock database of AccountHolder objects which will be available
to the user in the Banking language. 

We certify that this is our own original work

'''

import AccountHolder

class Bank:

  @staticmethod
  def initializeAccounts():

    # Array which will hold all of the bank accounts as a mock database
    accounts = []

    # Creates five bank accounts
    a1 = AccountHolder.AccountHolder(34567, "Melissa", "Brown", "MB123456")
    a2 = AccountHolder.AccountHolder(67890, "Obi-Wan", "Kenobi", "OK789045")
    a3 = AccountHolder.AccountHolder(123455, "Miku", "Hatsune", "MH908761")
    a4 = AccountHolder.AccountHolder(67890, "Frederick", "Frederickson", "FF908794")
    a5 = AccountHolder.AccountHolder(67890, "Enrique", "San-Capistrano", "ES5678903")

    # adds all accounts to the array
    accounts.append(a1)
    accounts.append(a2)
    accounts.append(a3)
    accounts.append(a4)
    accounts.append(a5)

    return accounts
    
    


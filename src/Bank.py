import AccountHolder

class Bank:
  allMyAccounts = []
  userChoice = 0
  continueBanking = True

  def initializeAccounts():
    accounts = []
    a1 = AccountHolder.AccountHolder(34567, "melissa", "brown", "MB123456")
    a2 = AccountHolder.AccountHolder(67890, "Obi-Wan", "Kenobi", "OK789045")
    a3 = AccountHolder.AccountHolder(123455, "Miku", "Hatsune", "MH908761")
    a4 = AccountHolder.AccountHolder(67890, "Frederick", "Frederickson", "FF908794")
    a5 = AccountHolder.AccountHolder(67890, "Enrique", "San-Capistrano", "ES5678903")
    accounts.append(a1)
    accounts.append(a2)
    accounts.append(a3)
    accounts.append(a4)
    accounts.append(a5)
    return accounts
    
  allMyAccounts = initializeAccounts()

  for account in allMyAccounts:
    print(account)
    print("balance: ", account.getBalance())
    print("After deposit of 55: ", account.deposit(55))
    print("After withdrawal of 10: ", account.withdraw(10))
    print("Trying to withdraw too much money: ", account.withdraw(1000000000000000000), "\n")


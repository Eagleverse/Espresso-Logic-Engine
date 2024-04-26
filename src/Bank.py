import AccountHolder

class Bank:
  allMyAccounts = []
  userChoice = 0
  continueBanking = True

  @staticmethod
  def initializeAccounts():
    accounts = []
    a1 = AccountHolder.AccountHolder(34567, "Melissa", "Brown", "MB123456")
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
    
    


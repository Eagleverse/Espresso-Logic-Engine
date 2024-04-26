class Statement:
    def __init__(self, program=None):
        self.Program = program
        self.Name = None
        self.Action = None
        self.Amount = None
        self.Account = None

    def evaluate(self, accounts):
        curAccount = next((x for x in accounts if x.accountID == self.Account), None)
        print(curAccount)
        if curAccount == None:
            raise ValueError("Account does not exist")
        elif self.Action == "withdraw":
            if self.Name != (curAccount.firstName + " " + curAccount.lastName):
                raise ValueError("Not authorized")
            else:
                self.Amount = self.Amount[1:]
                curAccount.withdraw(float(self.Amount))
                print(curAccount.getBalance())
        elif self.Action == "deposit":
            if self.Name != (curAccount.firstName + " " + curAccount.lastName):
                raise ValueError("Not authorized")
            else:
                self.Amount = self.Amount[1:]
                curAccount.deposit(float(self.Amount))
                print(curAccount.getBalance())

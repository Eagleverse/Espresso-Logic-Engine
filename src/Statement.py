'''
Brandon Pranke
Melissa Brown

CSC 330 Language Design and Implementation

4/28/2024

Week 7: Final Project

Defines a statement class. This represents the statement to be evaluated and a method that does the action in 
the statement

We certify that this is our own original work

'''
class Statement:
    #Statment fields are filled in by token values to represent the statment entered
    def __init__(self, program=None):
        self.Program = program
        self.Name = None
        self.Action = None
        self.Amount = None
        self.Account = None

    #Method for evaluated the statement takes a list already created accounts
    def evaluate(self, accounts):
        #Goes through the array of accounts to match the id to the id in the statement
        curAccount = next((x for x in accounts if x.accountID == self.Account), None)
        #Raises an error if no account exists
        if curAccount == None:
            raise ValueError("Account does not exist")
        #Checks the action of the attribute of the statement
        elif self.Action == "withdraw":
            #Checks if the correct name was given for the account 
            if self.Name != (curAccount.firstName + " " + curAccount.lastName):
                raise ValueError("Not authorized")
            else:
                #Calls the withdraw method and than prints the result
                self.Amount = self.Amount[1:]
                curAccount.withdraw(float(self.Amount))
                print(curAccount.getBalance())
        #Calls the deposit method and displays the result
        elif self.Action == "deposit":
            if self.Name != (curAccount.firstName + " " + curAccount.lastName):
                raise ValueError("Not authorized")
            else:
                self.Amount = self.Amount[1:]
                curAccount.deposit(float(self.Amount))
                print(curAccount.getBalance())

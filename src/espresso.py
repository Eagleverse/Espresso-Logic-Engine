'''
Names

CSC 330 Language Design and Implementation

(description)

Code is our own
'''

import Bank
import Lexer
import Program


bank = input("What bank action would you like to do?")
print(bank)
accessibleAccounts = Bank.Bank.initializeAccounts()
Program.Program.parse(Lexer.Lexer.lex(bank)).Statement.evaluate(accessibleAccounts)
'''
Brandon Pranke
Melissa Brown

CSC 330 Language Design and Implementation

4/28/2024

Week 7: Final Project

Uses the Lexer, Parser, and Program classes to run our own Banking language

We certify that this is our own original work

'''

import Bank
import Lexer
import Program

# User is expected to input something with the following syntax:
# [(name) (name) (withdraw/deposit) ($amount) (account number)]
# Examples:
#   Melissa Brown deposit $112.56 MB123456
#   Brandon Pranke withdraw $1000.00 BP256789
bank = input("What bank action would you like to do?")

# Creates accounts array for accounts that a user has access to, like a mock "bank"
accessibleAccounts = Bank.Bank.initializeAccounts()

# The lexer lexes the input (Lexer.Lexer.lex)
# The tokens are parsed (Program.Program.parse)
# The Statement attribute from the parsed tokens in the Program class are evaluated by the 
# "evaluate" function from the Statement class, where the Account Holder objects and functions
# are invoked to perform actions based on the users wishes
Program.Program.parse(Lexer.Lexer.lex(bank)).Statement.evaluate(accessibleAccounts)
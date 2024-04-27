'''
Brandon Pranke
Melissa Brown

CSC 330 Language Design and Implementation

4/28/2024

Week 7: Final Project

Defines a program class that represents the program in an AST. Also includes the parser method that
takes tokens and returns a program and statment object with tokens values filled in

We certify that this is our own original work

'''
from Statement import Statement
from Token import Token
from Lexer import Lexer
import Bank

class Program:
    #holds a statment field for the statement will be executed from the program 
    def __init__(self):
        self.Statement = None
    
    #Method for the parser
    #Takes tokens as a argument 
    @staticmethod
    def parse(tokens):
        #Creates a program object to represent the program
        program = Program()
        #Creates a Statement object to represent the statement in the program
        program.Statement = Statement(program)  
        
        #Sets up the current variable as null, used to keep track of what part of the statment, we are in
        current = None
        #Goes through all the tokens given
        for token in tokens:
            #If token is of type name than it current is equal to the statment and the statement fills in the name field
            if token.type == Token.NAME:
                #Checks to make sure the token is at the start of the statment
                if current is not None:
                    raise ValueError("Invalid syntax, statements must be of the form (name action amount account)")
                else:
                    current = Statement(program) 
                    current.Name = token.value 
                    
            #Fills in the action field in statement for tokens of action type
            elif token.type == Token.ACTION:
                if current is None:
                    raise ValueError("Invalid syntax, action must follow a name")
                else:
                    current.Action = token.value
                    
            #Fills in the amount field in statement for tokens of amount type
            elif token.type == Token.AMOUNT:
                if current is None:
                    raise ValueError("Invalid syntax, amount must follow an action")
                else:
                    current.Amount = token.value
                    
            #Fills in the account field in statement for tokens of account type
            #Resets current back to null in case there are more statements 
            elif token.type == Token.ACCOUNT:
                if current is None:
                    raise ValueError("Invalid syntax, account must follow an amount")
                else:
                    current.Account = token.value
                    program.Statement = current 
                    current = None  
                    
            else:
                raise ValueError("Invalid token type")
        #Returns the created program object which holds the statement object with information from the tokens
        return program
        
        
    
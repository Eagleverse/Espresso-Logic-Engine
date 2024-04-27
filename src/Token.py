'''
Brandon Pranke
Melissa Brown

CSC 330 Language Design and Implementation

4/28/2024

Week 7: Final Project

Creates a token class that defines the types of tokens used.

We certify that this is our own original work

'''


class Token:
    #TOKEN TYPES
    NAME = "Name" 
    ACTION = "Action"
    AMOUNT = "Amount"
    ACCOUNT = "Account"

    #Initializer
    def __init__(self, type, value, column):
        self.type = type
        self.value = value
        self.column = column
    
    #Function for displaying the token in a neater way
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

  
    
    
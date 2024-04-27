'''
Brandon Pranke
Melissa Brown

CSC 330 Language Design and Implementation

4/28/2024

Week 7: Final Project

Lexer class which takes in a line of code to find and return the tokens within

We certify that this is our own original work

'''

import re
from Token import Token


class Lexer:
    @staticmethod 
    def lex(text):

        # array to hold all found tokens
        tokens = []
        for line in text.split('\n'):
            if not line:
                continue

            # keeps track of where in the line we have already checked for tokens
            last_pos = 0
            
            # Checks for a name
            # Two words, each must begin with capital letter, only letters allowed
            # Valid: Melissa Brown, Brandon Pranke
            # Invalid: Melissa, brandon pranke
            match = re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', line)

            if match:
                # value is retrieved from match
                name = match.group(0)
                # token object is created with "name" value and added to tokens array
                tokens.append(Token(Token.NAME, name, last_pos))
                # position tracker is moved to the end of the match so that the rest of the line can be checked
                last_pos = match.end()
            else:
                # program is terminated if name is not correctly formatted
                raise ValueError("Line must begin with a name")

            # The part of the line which was already checked is removed from the string
            line = line[last_pos:].strip()
            
            # checks for a valid action
            # must be 'withdraw' or 'deposit'
            # Valid: "Melissa Brown withdraw..", "Brandon Pranke despoit..."
            # Invalid: "Peter Parker steal..."
            match = re.match(r'^(withdraw|deposit)', line)
            if match:
                # value is retrieved from match
                action = match.group(0)
                # token object is created with "action" value and added to tokens array
                tokens.append(Token(Token.ACTION, action, last_pos))
                last_pos = match.end()
            else:
                raise ValueError("Action is invalid. There must be an action")
            line = line[last_pos:].strip()
            
            # checks for valid dollar amount
            # Must being with dollar sign ($), have a decimal point, and 2 numbers after
            # Valid: ".... $1.12",".... $5000.45"
            # Invalid: "... 1", ".... 145.56"
            match = re.match(r'^(\$\d+\.\d{2})', line)
            if match:
                amount = match.group(0)
                tokens.append(Token(Token.AMOUNT, amount, last_pos))
                last_pos = match.end()
            else:
                raise ValueError("Amount is invalid. There must be an amount")
            line = line[last_pos:].strip()
            
            # Checks for valid account number
            # Must begin with 2 capital letters and be followed by 6 digits
            # Valid: "...MB123456", "CC567890"
            # Invalid: "... mb123456", "...CD123"
            match = re.match(r'^[A-Z]{2}\d{6}$', line)
            if match:
                account = match.group(0)
                tokens.append(Token(Token.ACCOUNT, account, last_pos))
                last_pos = match.end()
            else:
                raise ValueError("Account number is invalid. line must end with Account number ")

        # returns array with discovered tokens if no errors were raised
        return tokens
    
        
import re
from Token import Token
import Parser

class Lexer:
    @staticmethod #staticmethod
    # parse all the things
    def lex(text):

        # boolean
        valid_session = True
        tokens = []

        for line in text.split('\n'): # mel brown dep 5 bucks in acc
            # Check if the line is empty
            if line:
               last_pos = 0
            else:
                valid_session = False
            # Search for name at start of line and add it as a token
            match = re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', line)
            if (match != None) & valid_session: 
                name = match.group(0)
                tokens.append(Token(Token.NAME, name, 0))
                last_pos = match.end()
                print("Success")
            else:
                print("Line must begin with a name")
                valid_session = False
            line = line[last_pos:].strip()
            print(line)
            match = re.match(r'((withdraw)|(deposit)|(create))\s\$\d+\.\d{2}', line)
            if (match != None) & valid_session:
                action = match.group(0)
                tokens.append(Token(Token.ACTION, action, 0))
                last_pos = match.end()
                print("Success")
            else:
                print("action is bad")
                valid_session = False # terminate loop 
            line = line[last_pos:].strip()
            match = re.match(r'^[A-Z]{2}\d{6}', line)
            if (match != None) & valid_session:
                account = match.group(0)
                tokens.append(Token(Token.ACCOUNT, account, 0))
                last_pos = match.end()
                print("Success")
                line = line[last_pos:].strip()
            else:
                print("account does not match")
                valid_session = False

        return tokens if valid_session else [] 
        # return tokens

    
    myTokens = lex("Melissa Brown withdraw $150.00 MB123456")
    print(myTokens)

    if (myTokens != []):
        myParser = Parser.Parser()
        myParser.parse(myTokens)
    else:
        print("invalid tokens")
    
    
        
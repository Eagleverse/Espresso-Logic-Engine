import re
from Token import Token

class Lexer:
    @staticmethod #staticmethod
    # parse all the things
    def lex(text):
        # while thing is true
        # ruh oh thing is bad 
        # Quit, boot user to start
        # goals
        # match is good 👍

        # boolean
        valid_session = True
        # We're looking for an excuse to make this false and boot
        # the user out. Extra secure 🤌🤌🤌
        tokens = []
        # start y'alls loop

        while(valid_session):
            for line in text.split('\n'): # mel brown dep 5 bucks in acc
                # Check if the line is empty
                if line:
                    last_pos = 0
            
                    # Search for name at start of line and add it as a token
                    match = re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', line)
                    if match: 
                        name = match.group(0)
                        # What does this do?
                        tokens.append(Token(Token.NAME, name, 0))
                        # Explain
                        last_pos = match.end()
                        print("Success")
                        # Warning, could be a bad time.
                    else:
                        print("Line must begin with a name")
                        valid_session = False # terminate loop 🪦 
                    # search action
                    # trim what was name
                    # ["Name","Action","yada yada"]
                    line = line[last_pos:].strip()
                    print(line)
                    match = re.match(r'(withdraw)|(deposit)|(create)',line)
                    if match:
                        action = match.group(0)
                        # What does this do?
                        tokens.append(Token(Token.NAME, name, 0))
                        # Explain
                        last_pos = match.end()
                        print("Success")
                        # Warning, could be a bad time.
                    else:
                        print("action is bad")
                        valid_session = False # terminate loop 🪦 

        return tokens # I'm outside whiel loop

    
    lex("James Vooo deposit")
    
    
        
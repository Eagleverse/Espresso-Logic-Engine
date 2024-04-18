import re
from Token import Token

class Lexer:
    
    @staticmethod
    def lex(text):
        tokens = []
        
        for line in text.split('\n'):
            # Check if the line is empty
            if line:
                last_pos = 0
        
                # Search for name at start of line and add it as a token
                match = re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', line)
                if match:
                    name = match.group(0)
                    tokens.append(Token(Token.NAME, name, 0))
                    last_pos = match.end()
                    print("Success")
                
                else:
                    print("Line must begin with a name")
        
        return tokens
    
    lex()
    
    
        
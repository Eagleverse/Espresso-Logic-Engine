import re
from Token import Token


class Lexer:
    @staticmethod #staticmethod
    # parse all the things
    def lex(text):
        tokens = []
        for line in text.split('\n'):
            if not line:
                continue  # Skip empty lines
            last_pos = 0
            
            match = re.match(r'^[A-Z][a-z]+ [A-Z][a-z]+', line)
            if match:
                name = match.group(0)
                tokens.append(Token(Token.NAME, name, last_pos))
                last_pos = match.end()
            else:
                raise ValueError("Line must begin with a name")

            line = line[last_pos:].strip()
            
            match = re.match(r'^(withdraw|deposit|create)', line)
            if match:
                action = match.group(0)
                tokens.append(Token(Token.ACTION, action, last_pos))
                last_pos = match.end()
            else:
                raise ValueError("Action is invalid. There must be an action")
            line = line[last_pos:].strip()
            
            match = re.match(r'^(\$\d+\.\d{2})', line)
            if match:
                amount = match.group(0)
                tokens.append(Token(Token.AMOUNT, amount, last_pos))
                last_pos = match.end()
            else:
                raise ValueError("Amount is invalid. There must be an amount")
            line = line[last_pos:].strip()
            
            
            match = re.match(r'^[A-Z]{2}\d{6}$', line)
            if match:
                account = match.group(0)
                tokens.append(Token(Token.ACCOUNT, account, last_pos))
                last_pos = match.end()
            else:
                raise ValueError("Account number is invalid. line must end with Account number ")

        return tokens
        # return tokens

    
    # myTokens = lex("Melissa Brown withdraw $150.00 MB123456")
    # print(myTokens)
    
        
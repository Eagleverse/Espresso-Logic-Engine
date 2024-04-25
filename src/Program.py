from Statement import Statement
from Token import Token
from Lexer import Lexer

class Program:
    def __init__(self):
        self.Statement = None
    
    @staticmethod
    def parse(tokens):
        program = Program()
        program.Statement = Statement(program)  
        
        current = None
        for token in tokens:
            if token.type == Token.NAME:
                if current is not None:
                    raise ValueError("Invalid syntax, statements must be of the form (name action amount account)")
                else:
                    current = Statement(program) 
                    current.Name = token.value 
                    
            elif token.type == Token.ACTION:
                if current is None:
                    raise ValueError("Invalid syntax, action must follow a name")
                else:
                    current.Action = token.value
                    
            elif token.type == Token.AMOUNT:
                if current is None:
                    raise ValueError("Invalid syntax, amount must follow an action")
                else:
                    current.Amount = token.value
                    
            elif token.type == Token.ACCOUNT:
                if current is None:
                    raise ValueError("Invalid syntax, account must follow an amount")
                else:
                    current.Account = token.value
                    program.Statement = current 
                    current = None  
                    
            else:
                raise ValueError("Invalid token type")
        print(program.Statement.Name) 
        return program
    
myTokens = Lexer.lex("Melissa Brown withdraw $1.25 MB123456")

parsedStatement = Program.parse(myTokens)
        
        
    
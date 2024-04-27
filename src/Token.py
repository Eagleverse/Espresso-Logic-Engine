


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
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

  
    
    
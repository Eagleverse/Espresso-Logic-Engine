


class Token:
    #TOKEN TYPES
    NAME = "Name" 
    ACTION = "Action"
    ACCOUNT = "Account"
    # :)
    # lil function to print tokens
    # Next = profit

    #Initializer
    def __init__(self, type, value, column):
        self.type = type
        self.value = value
        self.column = column
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

    # If exists return the things
    # token token object object ??? lol
    # S T E A L
    
    
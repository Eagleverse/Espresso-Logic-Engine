


class Token:
    #TOKEN TYPES
    NAME = "Name"
    
    #Initializer
    def __init__(self, type, value, column):
        self.type = type
        self.value = value
        self.column = column
    
    
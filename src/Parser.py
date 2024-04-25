class Parser:
    @staticmethod
    def parse(tokens):
        print(tokens[0].value)
        actionTokens = tokens[1].value.split()
        print(actionTokens[0])
        print(actionTokens[1])
        print(tokens[2].value)
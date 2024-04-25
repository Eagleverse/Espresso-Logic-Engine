from Token import Token
import AccountHolder

class Parser:
    @staticmethod
    def parse(tokens):
        current = []
        i = 0
        print("\n\nbeginning parser")
        for token in tokens:
            if token.type == Token.NAME:
                current.append(token.value)
                # print(current[i])
                i += 1
            elif token.type == Token.ACTION:
                actionTokens = token.value.split()
                current.append(actionTokens[0])
                # print(current[i])
                i += 1
                current.append(float(actionTokens[1][1:]))
                # print(current[i])
                i += 1
            elif token.type == Token.ACCOUNT:
                current.append(token.value)
                # print(current[i])
        
        if (current[1] == "withdraw"):
            fullName = current[0].split()
            accountNumber = fullName[0][0] + fullName[1][0] + "123456"
            a1 = AccountHolder.AccountHolder(1000, fullName[0], fullName[1], current[3])
            a1.withdraw(current[2])
            print(a1.getBalance())
        elif (current[1] == "deposit"):
            fullName = current[0].split()
            accountNumber = fullName[0][0] + fullName[1][0] + "123456"
            a1 = AccountHolder.AccountHolder(0, fullName[0], fullName[1], current[3])
            a1.deposit(current[2])
            print(a1.getBalance())
            print("deposit")
        elif (current[1] == "create"):
            fullName = current[0].split()
            print(fullName[0][0])
            accountNumber = fullName[0][0] + fullName[1][0] + "123456"
            print(accountNumber)
            a1 = AccountHolder.AccountHolder(current[2], fullName[0], fullName[1], current[3])
            print(a1)
            print("create")
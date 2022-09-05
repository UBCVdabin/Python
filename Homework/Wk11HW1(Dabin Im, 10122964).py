class Account():

    def __init__(self, id = 0, balance = 100.0, annualInterestRate = 0.0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def __str__(self):
        text  = "ID                    : " + str(self.id) + "\n"
        text += "Balance               : " + str(self.balance) + "\n"
        text += "Monthly Interest Rate : " + str(self.getMonthlyInterestRate() * 100) + " %\n"  # because of percentage.
        text += "Monthly Interest      : " + str(self.getMonthlyInterest())

        return text

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 1200

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

    def withdraw(self, amount):
        if self.balance < amount:
            self.isSuccess(False)
        else:
            self.isSuccess(True)
            self.balance -= amount
        
        self.showBalance()
    
    def deposit(self, amount):
        self.balance += amount

        self.showBalance()

    def isSuccess(self, Success):
        if Success:
            print("Your Request is Succeeded.")
        else:
            print("[Error] Your request is failed. Check your Balance.")

    def showBalance(self):
        print("Your Balance : " + str(self.balance))


def main():
    test = Account(1122, 20000, 4.5)
    test.withdraw(2500)
    test.deposit(3000)
    print()
    print(test)

main()
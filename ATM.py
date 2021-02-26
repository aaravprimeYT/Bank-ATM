class Atm:
    def __init__(self, cardNumber, pin):
        self.cardNumber = cardNumber
        self.pin = pin

    def checkBalance(self):
        print("Your Balance is 10000")

    def withdraw(self, amount):
        newAmount = 10000 - amount
        print("You have withdrawn " + str(amount) + ' ' + "Your remaining balance is " + str(newAmount))

def main():
    cardNumber = input("Insert Your Card Number: ")
    pinNumber = input("Enter Your Pin Number: ")
    newUser = Atm(cardNumber, pinNumber)

    print("Choose Your Activity")
    print("1. Balance Enquiry, 2. Withdraw")
    activity = int(input("Enter Activity Number: ")) 

    if(activity == 1):
        newUser.checkBalance()
    elif(activity == 2):
        amount = int(input("Enter The Amount: "))
        newUser.withdraw(amount)
    else:
        print("Enter A Valid Number")
        
main()
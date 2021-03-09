'''
Imagine you are designing a banking application. What would a
customer look like? What attributes would she have? What methods
would she have?
'''

class Bank():
    def __init__(self):
        self.amount = int(input('Enter the amount of money you have'))

    def deposite_money(self,money):
        self.amount = self.amount + money
        return f"You have deposited {money} amount"

    def withdraw_money(self,withdraw):
        self.amount = self.amount - withdraw
        return f"You have withdrawn {withdraw} amount"

    def total_money(self):
        return f'Your total balance is {self.amount}'


customer = Bank()
print(customer.deposite_money(int(input('Enter sum of money you want to deposite:'))))
print(customer.withdraw_money(int(input('Enter amount you want to withdraw:'))))
print(customer.total_money())
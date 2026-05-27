#Sophia Chen
#Init
balance = 1000

def deposit():
    global balance
    money = int(input("Enter the amount you would like to deposit: "))
    balance = balance + money

def withdraw():
    global balance
    money = int(input("Enter the amount you would like to withdrawal: "))
    balance = balance - money
def display_total():
    print("Your total:"+" "+str(balance))

#Main
deposit()
withdraw()
display_total()

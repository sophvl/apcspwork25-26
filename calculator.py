#Sophia Chen
#Calculator

#Function
def main():
    #Welcome message
    print("Welcome to my simple calculator!")
    #Collect input
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    operator = input("Please enter an operator(+, -, *, /): ")
    #Perform Operation
    if operator == "+":
        print(calc_sum(num1,num2))
    elif operator == "-":
        print(calc_sub(num1,num2))
    elif operator == "*":
        print(calc_mult(num1,num2))
    else:
        print(calc_div(num1,num2))
#This function adds two numbers and return the total
def calc_sum(x,y):
    return x + y
def calc_sub(x,y):
    return x - y
def calc_mult(x,y):
    return x*y
def calc_div(x,y):
    return x/y
#Main
main()

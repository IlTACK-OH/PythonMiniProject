# Caculator project
import os
from art import logo
# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1*n2

# Divide
def divide(n1, n2):
    return n1/n2

def calculate(n1,operations):
    operations_symbol = input("Pick an operation: ")
    while True:
        if operations_symbol not in operations:
            operations_symbol = input("Not valid operation. Pick an operation again: ")
        else:
            break
    n2 = float(input("What's the next number?: "))
    answer = operations[operations_symbol](n1, n2)
    print(f"{n1} {operations_symbol} {n2} = {answer}")
    return answer

# calculation dictionaly
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
continue_answer ='y' # 반복문 처음 시작을 위한 변수
while True:
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    while continue_answer =='y':
        answer = calculate(num1, operations)
        continue_answer = input("Type 'y' to continue calculating wiht {answer}, or type anything to start a new calculation: ")
        num1 = answer
    os.system('clear')
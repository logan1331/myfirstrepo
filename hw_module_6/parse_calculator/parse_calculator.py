# This is small program of calculator which using parsing techniques and import modules

import argparse
import getpass
import math
import operations as op

def main():
    
    # Using the argparse module is creating an ArgumentParser object
    parser = argparse.ArgumentParser()
    
    # Adding arguments by using add_argument method
    parser.add_argument("-n1",'--number1', type=int, default=0,
                        help= "Enter number 1! (Ex. '1','2...')")

    parser.add_argument("-n2",'--number2', type=int, default=0,
                        help= "Enter number 2! (Ex. '1','2...')")

    parser.add_argument("-o", '--operation', type=str, default='+',
                        help= "Define the operation above the numbers (Ex. '+', '-')")

    # ArgumentParser parses arguments through the parse_args() method
    args = parser.parse_args()
    
    # Passing parameter keys
    num1 = args.number1
    num2 = args.number2
    operation = args.operation

    
    print('Parcer initialized!')
    print(f"{num1=}, {num2=}, {operation=}")
    
    # Defining an operation and calling a function
    if operation == '+':
        print(f"The result is: {op.add(num1, num2)}")

    if operation == '-':
        print(f"The result is: {op.sub(num1, num2)}")

    if operation == '*':
        print(f"The result is: {op.mul(num1, num2)}")

    if operation == '/':
        print(f"The result is: {op.div(num1, num2)}")

# Checking the main file by using exception
if __name__ == '__main__':
    try: 
        main()
    except Exception:
        print("Something wrong!!!")

    
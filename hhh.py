while True:
    print("welcome!")
    print("my options:")
    print("enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    if user_input == "quit":
        print("kharej shod")
        break
    elif user_input == "add":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 + num2)
        print("your answer:"+ result)
    elif user_input == "subtract":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 - num2)
        print("your answer:"+ result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 * num2)
        print("your answer:"+ result)
    elif user_input == "divide":
        num1 = float(input("Enter a number:"))
        num2 = float(input("Enter another number:"))
        result = str(num1 / num2)
        print("your answer:"+ result)
    else:
        print("Error :(")
        

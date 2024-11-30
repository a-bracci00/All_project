while True:
    chiudi = input('continuare?')
    if chiudi == 'no':
        break
    # Ask the user for the first number
    first_num = input("Enter the first number: ")

    # Ask the user for the second number
    second_num = input("Enter the second number: ")

    # Ask the user for the operation they want to perform
    operation = input("Enter the operation (+, -, *, /): ")

    # Use the eval() function to evaluate the expression
    result = eval(first_num + operation + second_num)

    # Print the result
    print(result)

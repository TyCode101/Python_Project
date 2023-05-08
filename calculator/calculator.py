# This is a very basic calculator program that takes in float numbers

# Starts the program

while True:

# Prompt for user input


    Num1 = float(input("Enter the first number: "))

    Num2 = float(input("Enter the second number: "))


# Perform operations

    print("Sum: {} + {} = {}".format(Num1, Num2, Num1 + Num2))
    print("Difference: {} - {} = {}".format(Num1, Num2, Num1 - Num2))
    print("Product: {} * {} = {}".format(Num1, Num2, Num1 * Num2))
    print("Divison: {} / {} = {}".format(Num1, Num2, Num1/Num2))

    end = input("Would you like to continue? Please type either yes or no here: ")
    


    if end == "no":
        exit()

    if end == "yes":
        continue
    
    if end != "no":
        end = input("Invalid response, please type either yes or no: ")
        
        
    if end != str:
        end = input("Invalid response, please type either yes or no: ")
        
            

    


# source by: https://phoenixap.com/kb/python-calculator


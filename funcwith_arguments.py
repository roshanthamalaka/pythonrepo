# Here Function created with arguments and use default values with arguments 

def add_numbers(num1=50,num2=50):
    num1 = float(num1)
    num2 = float(num2)
    total = num1+num2
    return total

# Overide default values
tot = add_numbers(10,20)

print("Total is ",tot)


# Use default values
tot = add_numbers()

print ("Default Total is",tot)


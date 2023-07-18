#Use of Global Variables 

def printVariable():
    global number
    number= 100

printVariable() # Call the function. Without calling the function give variable undeclared  during runtime

print ("Number throguh function global variable is ",number)
try: 
    x = int(input("Enter Number "))
    y = 1/x
    print("One Dived by Value is ",y)

# ZeroDivisionError and ValueError are the predefined execeptions 

except ZeroDivisionError:
    print ("Division By Zero") # When divide by Zero
except ValueError: 
    print ("Please enter an Integer")  # Execute when user input a string 
except: 
    print ("Something else is wrong") # Any other exception occured 


print ("All Done")
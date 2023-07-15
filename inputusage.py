number= input ("Enter a Number ")

number = int(number) *100 # Need to convert to integer using type casting because every input considered as string

#Use Plus mark with Variable
print("Your Entered number Multiply by 100 is:  "+ str(number))  # Converted to float to string because print only accept string

# Integer does not allowed decimal so entered number converting float 

number = float(number) /3 

print ("Entered Number Multiply by 100 and Divied by 3 is "+str(number))
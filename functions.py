def print_poster():
    print ("Nidimatai Hutto")


print_poster( ) # Invoke the Function


def input_bday():
   bday =int(input("Enter Your Birthday: "))
   value = bday % 4 # Use modules division to check whether there is remainder 

   if (value == 0):
       print ("You Were born Extra Year")
   else:
        print("You Did not born on Extra Year")

input_bday() # Calling The Function


letters = ["A","B","C","D","E"]

firstTwo = letters[0:2]

print(firstTwo) 

print(letters[1:]) #  ['B', 'C', 'D', 'E']

print(letters[:3]) # ['A', 'B', 'C']

print(letters[1:-1]) # ['B', 'C', 'D']

print(letters[:]) # ['A', 'B', 'C', 'D', 'E']

del letters[1:3] 

print (letters) # ['A', 'D', 'E']

del letters[:] # Entire list get deleted So print an empty list

print (letters)

# Dictionary is data type which use key value pairs

usernames = {
    "Lydia" : "GroP@134",
    "Sarah" : "Tag4@4",
    "Mike"  : "Tyson"


}

print("Printing Value using Key Lydia")
print(usernames["Lydia"])

print("Printing Keys in the dictionary using keys method")
print(usernames.keys())


print("Printing Values using value method")
print(usernames.values())


print("Get all the items in the dictionary using items method")
print(usernames.items())

print("Update Value in Dictionary using key. Key is max")
usernames["max"] = "Pane@4453"
print(usernames)

print("Insert Data to the Dictionary using update method")
usernames.update({"Chole":"Williams224"})
print(usernames)

print("Delete Item in a dictionary using del keyword")
del usernames["max"]
print(usernames)


print("Delete the last items from the dictionary using popitem")
usernames.popitem()
print(usernames)

print("Clear all the items in the dictionary using clear ")
usernames.clear()
print(usernames)
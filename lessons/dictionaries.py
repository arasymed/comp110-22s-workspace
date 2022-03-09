"""Demostrations of dictionary capabilities."""


# Declaring the type of a dictionary.
schools: dict[str, int]

# Initialize to an empty dictionary, could do both steps together (1 and 2), this is just demostration.
schools = dict()
# This says go contruct a new dictionary for me. So we call dictionary's CONSTRUCTOR FUNCTION

# Set a key-value pairing in the dictionary
schools["UNC"] = 19_400
# 19_400 is an integer literal
# We can set up other entries as well
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Acess a value by its key -- "lookup"
print(schools["UNC"])
# We can make it a string
print(f"UNC has {schools['UNC']} students")
# Strings are permitted to use single quotes or double questes
# Here for example we use single quotes because we already used double quotes for the concatenation, so we cannot use double quotes for "UNC" again
# We use single quotes for 'UNC' look up
# When we write schools['UNC'] we are looking up some specific string index

# Remove a key-value pair from a dictionary 
# By its key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
# We are asking: is the key in schools?
print(f"Duke is present: {is_duke_present}")
# We can use this in if statements as well
if "Duke" in schools:
    print("Foun the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

print(schools) 
# In this print we see that there is no duke in the dictionary. (Just to clarify)

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] = schools["NCSU"] + 200
# Here we are using relative reasignment we can change it to schools["NCSU"] += 200 instead as well


# Demostration of dictionary literals
# Example of empty dictionary literal
schools = {}  # sane as constructor dict()
print(schools)

# Alternatively, initialize key-value pairs
school = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
# This is one way to initialize it
# We could use white space to make it easier to read like this
schools = {
    "UNC": 19400,
    "Dukie": 6717,
    "NCSU": 26150
}
print(schools)

# Access a key that does not exists
print(schools["UNCC"])
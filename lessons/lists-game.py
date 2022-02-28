"""Examples of using lists in a simple 'game'."""



from random import randint 

rolls: list[int] = list()

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:  # while the last roll is not equal to 1 we keep looping
    rolls.append(randint(1, 6))  # until we roll a 1 we want to keep appending another roll to out list

print(rolls)

# Remove an item from the list by its index ("pop")
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i = i + 1

print(f"Total score: {sum}")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Acess an individual item
# print(rolls[0])

# # Acess the lenght of a list (number of items)
# print(len(rolls))

# # Acess the last item of a list
# last_index: int = len(rolls) - 1
# print(rolls[len(rolls) - 1])
# print(rolls[last_index])
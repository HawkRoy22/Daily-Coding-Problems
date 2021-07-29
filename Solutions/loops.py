
# Print all elements of a list using for loop.
word = [1,2,3,4,5,6]
for i in word:
    print(i)

#Take inputs from user to make a list.
# Again take one input from user and search it in the list and delete that element, if found.
# Iterate over list using for loop.
players = ["Roger Federer", "Rafael Nadal", "Novak Djokovic"]
for i in players:
    for x in players:
        if i != x:
            print(i + ' VS ' + x)

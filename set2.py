#20ce115 divya prajapati
#Write a Python program to remove an item from a set if it is present in the set.
#Create a new set
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
#printing the original set
print(num_set)
print("\nRemove 0 from the said set:")
#discarding a partivular element from the set
num_set.discard(0)
print(num_set)
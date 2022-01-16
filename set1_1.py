#20ce115 divya prajapati
#Write a Python program to add member(s) in a set and clear a set
#A new empty set
color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
#ADDING SINLE ELEMENT IN SET
print(color_set)
#clearing set
color_set.pop()
print("\nafter clearing the original set and adding new element in the set:")
#ADDING ELEMENT IN SET
color_set.update(["Blue", "Green"])
print(color_set)
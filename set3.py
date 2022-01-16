#20ce115 divya prajapati
#Write a Python program to create an intersection, Union, difference of sets.
#creating two sets
setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
#printing original two sets
print(setx)
print(sety)
#intersectin of two sets
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)
#union of two sets
print("\nunion of two said sets:")
setc = setx.union(sety)
print(setc)
#difference of two sets
print("\ndifference of two said sets:")
setd = setx.difference(sety)
print(setd)

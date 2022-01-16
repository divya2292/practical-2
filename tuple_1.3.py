"""DIVYA PRAJAPATI - 20CE115
Write a Python program to add an item in a tuple."""
a1=input("enter 1st number :")
a2=input("enter 2nd number :")
a3=input("enter 3rd number :")
a4=input("enter 4th number :")
a5=input("enter 5th number :")

myNumber=(a1,a2,a3,a4,a5)
print("original tuple is : ",myNumber)
#type casting tuple into list to perform append function
L1=list(myNumber)
#adding element at the end of the list
L1.append(6)
#type casting list into tuple to get the final output in tuple
T1=tuple(L1)
print("updated tuple is : ",T1)
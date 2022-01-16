"""DIVYA PRAJAPATI - 20CE115
Write a Python program to create a tuple with numbers and print one item. """
#taking input values from user
a1=input("enter 1st number :")
a2=input("enter 2nd number :")
a3=input("enter 3rd number :")
a4=input("enter 4th number :")
a5=input("enter 5th number :")



myNumber=(a1,a2,a3,a4,a5)
print(myNumber)
#printing number present on the second position
thirdNumber=myNumber[2]
print("The third element of tuple is : ",thirdNumber)

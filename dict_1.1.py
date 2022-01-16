"""DIVYA PRAJAPATI - 20CE115
 Write a Python script to check whether a given key already exists in a dictionary."""

#declaring a dictionary
dict1={
    "abc":"cba",
    "DIVYA":"GIRL",
    "php":"dictionary"
}
#taking any key from the dictionary
t1="okay"
#using if..in function to check whether given key is present in dictionary or not
if t1 in dict1:
    print(t1," is present")
else:
    print(t1," is absent")
"""DIVYA PRAJAPATI - 20CE115
Write a Python script to merge two Python dictionaries."""

dict1 = {
    "T1":"FIRST",
    "PHP":"DICTIONARY"
}
dict2 = {
    "ID" : 115,
    "NAME" : "DIVYA"
}
#creating a new dictionary and copying the elements of first dictionary
dict3 = dict1.copy()
#updating the new dictionary by merging all elements of second dictionary
dict3.update(dict2)
print("combined dictionary is : ",dict3)
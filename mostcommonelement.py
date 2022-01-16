#20ce115 - divya prajapati
#Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
list_of_words=['Cars', 'Cats', 'Flowers', 'Cats','Cats','Cats']
from collections import Counter
c = Counter(list_of_words)
#most common element in the list
c.most_common(1)
print ("",c.most_common(1))
#creating dictionary
input_dict = {'A': 1963, 'B': 1963, 'C': 1964, 'D': 1964, 'E': 1964, 'F': 1965, 'G': 1965, 'H': 1966, 'I': 1967, 'J': 1967, 'K': 1968, 'L': 1969 ,'M': 1969, 'N': 1970}
# in above code, `value` will hold value `1964` which is the most commn and `count` will hold value `3`
value, count = Counter(input_dict.values()).most_common(1)[0]
print(value,count)

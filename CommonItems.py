#finding common items in dictionaries. Could be keys, values or both.

a = {
 'x' : 1,
 'y' : 2,
 'z' : 3 
 }

b = {
 'w' : 10,
 'x' : 11,
 'y' : 2 }

#shows the common keys in both dicts (what is a and also in b)
print(a.keys() & b.keys())

#prints what is in a and not in b
print(a.keys() - b.keys())


# #this will throw an eror
# print(a.values() & b.values())
print('apple' > 'Apple')
print(ord('a'))
print(ord('A'))
print(chr(97))
print(chr(65))

num = [9, 7,  6, 15, 16, 5, 10, 11]
num.sort()
# sorted(massiv, argument) может работать также и со словарями
print(num)

orig_dict = {'b':1,'a':2,'c':3}
sorted_items = sorted(orig_dict.items())

sorted_dict = dict(sorted_items)
print(sorted_dict)


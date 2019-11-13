#create a list of the first 10 perfect squares
#with for statement

sq_list = []
for x in range(1,11):
    sq_list.append(x * x)
print(sq_list)

#with list comprehension

new_list = [x * x for x in range(2, 10) if x % 2 != 1]
print(new_list)

##transforming list comprehension in simple for statement
print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])

a = []
for ch in 'comprehension':
    if ch not in 'aeiou':
        a.append(ch.upper())
print(a)
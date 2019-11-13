#1. Modify the given code so that the final list only contains a single copy of each letter.
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

word_list = ['cat', 'dog', 'rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list:
            letter_list.append(a_letter)
print(letter_list)

#2. Redo the given code using list comprehensions. For an extra challenge, see if you can
#figure out how to remove the duplicates.
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'a','b', 'b', 'i', 't']  
new_list = ['cat', 'dog', 'rabbit']
chars = [char for word in new_list for char in list(word)]
l_list = [i for i in chars if i not in chars] 
print(l_list)
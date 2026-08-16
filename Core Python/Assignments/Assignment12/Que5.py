#Que5.Python Program to count the Number Of Vowels in a string

#Without using Method
# s=input('Enter String:')
# count=0
# for i in s:
#     if i in 'aeiouAEIOU':
#         count=count+1
# print('Number of Vowels=',count)

#With using Method
s=input('Enter String:')
count=s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')+s.count('A')+s.count('E')+s.count('I')+s.count('O')+s.count('U')
print('Number of Vowels=',count)
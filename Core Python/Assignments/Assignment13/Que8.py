#Que8.Python Program to count the Frequency of words Appearing in a string using Dictionary

s=input('Enter String:')
words=s.split()
d={}
for word in words:
    if word in d:
        d[word]=d[word]+1
    else:
        d[word]=1
print('Word Frequency=',d)

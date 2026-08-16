#Que14.Python Program to count the occurence of each word in string.

s=input('Enter String:')
words=s.split()
for i in range(len(words)):
    count=0
    if words[i] not in words[:i]:
        for j in words:
            if words[i]==j:
                count+=1
        print(words[i],'=',count)

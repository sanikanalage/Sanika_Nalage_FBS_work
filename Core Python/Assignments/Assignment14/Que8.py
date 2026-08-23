#Que8.Write a Python Program to find all the anagrams and group them together from a given list of strings.

strings = ["eat", "tea", "tan", "ate", "bat", "aab", "nat","aba"]

groups = []

for word in strings:
    found = False

    for group in groups:
        if len(word) == len(group[0]):

            is_anagram = True

            for ch in set(word):
                if word.count(ch) != group[0].count(ch):
                    is_anagram = False
                    break

            if is_anagram:
                group.append(word)
                found = True
                break

    if not found:
        groups.append([word])

print('List:',strings)
print("Grouped Anagrams:")

for group in groups:
    print(group)
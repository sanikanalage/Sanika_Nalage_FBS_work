#Write a program to input any alphabet and check whether it is vowel or consonant

alphabet=input('Enter Alphabet:')
if(alphabet in 'aeiouAEIOU'):
    print('Vowel')
else:
    print('Consonant')
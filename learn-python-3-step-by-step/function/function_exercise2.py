def count_vowel(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 1
   
    for i in range(len(str)):
        if str[i] in vowels:
            count += 1     
    return count
   

v = count_vowel('aeiou')
print(v)
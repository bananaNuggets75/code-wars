""" Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiac", let's cross out the vowels. We get: "z o d ia c"

"zodiac" -> 26
The consonant substrings are: "z", "d" and "c" with values "z" = 26, "d" = 4 and "c" = 3. The highest is 26.

"strength" -> 57
The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest is 57.

For C: do not mutate input.

More examples in test cases. Good luck!

If you like this Kata, please try:

Word values

Vowel-consonant lexicon """

def solve(s):
    vowels = set('aeiou')
    max_sum = current_sum = 0
    
    for ch in s:
        if ch in vowels:
            current_sum = 0  # reset when vowel found
        else:
            current_sum += ord(ch) - 96
            max_sum = max(max_sum, current_sum)
    
    return max_sum


""" import re

def solve(s):
    return max(sum(ord(c)-96 for c in subs) for subs in re.split('[aeiou]+', s))

def solve(s):
    alphabet = "-abcdefghijklmnopqrstuvwxyz"
    for vowel in "aeiou":
        s = s.replace(vowel, " ")
    values = []
    for item in s.split():
        sum = 0
        for letter in item:
            sum += alphabet.index(letter)
        values.append(sum)        
    return max(values) 
    
    
import string
def solve(s):
    string_list=(list(s))
    alphabets=(list(string.ascii_lowercase))
    test=[]
    for i in range(1,len(alphabets)+1):
        test.append(i)
    my_dictionary=dict(zip(alphabets,test))
    vowels="aeiou"
    vowels_list=list(vowels)
    compare_list1=[]
    for i in range(len(string_list)):
        if string_list[i] in my_dictionary and string_list[i] not in vowels:
            l=(my_dictionary[string_list[i]])
            compare_list1.append(l)
        else:
            compare_list1.append("vowels")
            
    z=(compare_list1)
    x = []
    l = len(z)
    previous_element = 0
    count = 0
    if( isinstance(z[0] , int)  == True ):
            count = z[0]    
    elif( z[0] == 'vowels' ):
            previous_element = z[0]           
    for i in range(1,l):
        if( previous_element == 'vowels' ):
                if(count > 0):
                    x.append(count)
                count = 0       
        elif( isinstance( previous_element , int)  == True ):
                count = count + previous_element
        previous_element = z[i]       
    if( isinstance(z[l-1] , int)  == True ):
            count = count + previous_element
            x.append(count)    
    elif( z[l-1] == 'vowels' ):
            x.append(count)       
    print(x) 
    y=max(x)
    return y
        
solve("zodiacs")
"""
                

                
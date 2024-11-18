def count_vowels_and_consonants(S):
    vowels="aeiou"
    vowel_count=0
    consonant_count=0
    for char in S:
        if char.isalpha():
            if char.lower() in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    return f"{vowel_count},{consonant_count}"
S=input()
print(count_vowels_and_consonants(S))

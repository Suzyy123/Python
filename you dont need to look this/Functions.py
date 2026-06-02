#Write a function that takes a string and returns the count of vowels and consonants separately
def vowels_conso(word):
    vowels = "aeiouAEIOU"
    countVowels = 0
    countConsonants = 0
    for eachChar in word:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowels = countVowels + 1
            else:
                countConsonants = countConsonants + 1
    return countVowels, countConsonants

vowels, consonants = vowels_conso("sujita sankhar")
print(f"Vowels: {vowels}, Consonants: {consonants}")

#Define a function convert_to_upper(word) that returns the uppercase version of the string
def convert_to_upper(word):
    return word.upper()
print(convert_to_upper("sujitA sankhar"))
# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    if(sorted(word)== sorted(anagram)):

    
        print("Both strings are an Anagram.")
    else:
        print("Both strings are not an Anagram.")

find_anagram ("jump" "pmuj")
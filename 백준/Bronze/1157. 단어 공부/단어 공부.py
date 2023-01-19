from collections import Counter

def find_max(word):
    counter = Counter(word)
    max_count = -1

    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
        elif counter[letter] == max_count:
            max_letter += letter
    
    return max_letter


word = input().lower()

if len(find_max(word)) == 1:
    print(find_max(word).upper())
else:
    print("?")   
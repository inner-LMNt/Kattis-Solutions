word = input().lower()

vowels = set(['a', 'e', 'i', 'o', 'u'])
new_word = ''
has_l = False

# Simmer down the word into consonants, vowels and underscores
for letter in word:
    if letter == '_':
        new_word += letter
    elif letter == 'l':
        new_word += 'c'
        has_l = True # Condition for a pleasant word
    elif letter in vowels:
        new_word += 'v'
    else:
        new_word += 'c'

# No three sequential consonants or vowels allowed
def verify_word(word):
    if word.find('vvv') != -1:
        return False
    if word.find('ccc') != -1:
        return False
    return True

# Recursive function to fill in underscores
def helper(word, vowels_used, consonants_used):
    res = 0
    
    if word.find('_') == -1: # Base case, no underscores left
        if not verify_word(word): # Unpleasant word
            return 0
        
        # Combinatorics
        # Vowels can be freely picked from the 5. Consonants from the 21, except for the case where no 'l' is present
        total_combinations = pow(5, vowels_used) * (pow(21, consonants_used) - pow(20, consonants_used))
        return total_combinations
        
    index = word.find('_')
    
    res += helper(word[:index] + 'v' + word[index + 1:], vowels_used + 1, consonants_used) # Fill in with a v
    res += helper(word[:index] + 'c' + word[index + 1:], vowels_used, consonants_used + 1) # Fill in with a c

    return res

# Similar recursive function but for words with 'l'. Affects the math
def helper_with_l(word, vowels_used, consonants_used):
    res = 0

    if word.find('_') == -1: # Base case, no underscores left
        if not verify_word(word): # Unpleasant word
            return 0
        
        # Combinatorics
        # Vowels can be freely picked from the 5. Consonants from the all 21 since there is an 'l' already
        total_combinations = pow(5, vowels_used) * pow(21, consonants_used)
        return total_combinations
        
    index = word.find('_')
    
    res += helper_with_l(word[:index] + 'v' + word[index + 1:], vowels_used + 1, consonants_used) # Fill in with a v
    res += helper_with_l(word[:index] + 'c' + word[index + 1:], vowels_used, consonants_used + 1) # Fill in with a c

    return res


result = 0

if has_l:
    result = helper_with_l(new_word, 0, 0)
else:
    result = helper(new_word, 0, 0)

print(result)

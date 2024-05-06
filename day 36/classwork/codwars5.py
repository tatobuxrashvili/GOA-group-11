# write the function is_anagram
def is_anagram(test, original):
    word1 = sorted(test.lower())
    word2 = sorted(original.lower())
    return word1 == word2
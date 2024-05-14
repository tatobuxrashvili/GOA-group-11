def duplicate_encode(word):
    word = word.lower()
    j = []
    for i in word:
        if word.count(i) == 1:
            j.append('(')
        else:
            j.append(')')
    return ''.join(j)
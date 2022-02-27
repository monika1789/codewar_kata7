#  find vowels from the string


def get_count(sentence):
    sentence.split('  ')
    a = sentence.count('a')
    e = sentence.count('e')
    i = sentence.count('i')
    o = sentence.count('o')
    u = sentence.count('u')
    return a+e+i+o+u


# return sum(c in 'aeiou' for c in s)   
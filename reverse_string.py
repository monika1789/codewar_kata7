# Reverese the string

def reverse_words(s):
    s = s.split(" ")
    s = ' '.join (reversed(s))
    return s
        
#Write a Python program to count the occurrences of each word in a given sentence

from itertools import count


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word]+= 1
        else:
            counts[word] = 1

    return counts
print(word_count('the tops is higher education and tops is good. '))
from collections import Counter
import re

def count_words(line):
    wordregex=r"\b[-`'\w]+\b"
    words = re.findall(wordregex,line.lower())
    return Counter(words)


if __name__ == "__main__":
    print (count_words("don't stop believing!"))
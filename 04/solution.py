import os
from collections import Counter

input = 'aa bb cc dd ee'

#Making a list of words

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

def get_input_rows(fname):

    with open(fname) as f:
        content = f.read().splitlines()

    return content

def check_words(passphrases):

    valid = []

    for row in passphrases:
        dictionary = {}
        words = row.split()

        if not check_anagrams(words):
            valid.append(False)
        else:
            for word in words:
                if word not in dictionary:
                    dictionary[word] = 1
                elif word in dictionary:
                    dictionary[word] += 1

            if max(dictionary.values()) == 1:
                valid.append(True)
            else:
                valid.append(False)

    return valid

def check_anagrams(words):

    for i, word in enumerate(words):
        for j, check in enumerate(words):
            if i == j:
                continue
            elif Counter(word) == Counter(check):
                return False

    return True

def main():

    passphrases = get_input_rows(path)
    #wordlist = input.split()

    valid = check_words(passphrases)



    print 'There are {} valid passphrases, out of a total of {}.'.format(sum(valid), len(valid))

if __name__ == "__main__":
    main()

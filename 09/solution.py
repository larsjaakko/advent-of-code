import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

def get_input_rows(fname, integer = False):

    with open(fname) as f:
        content = f.read()

    if integer:
        content = map(int, content)

    return content

def calculate_score(stream):

    depth = 0
    score = 0
    garbage = False
    skip = False
    gbg_count = 0

    for i, char in enumerate(stream):

        if skip:
            skip = False
            continue

        if char == '!' and garbage:
            skip = True
            continue

        if char == '<' and not garbage:
            garbage = True
            continue

        if char == '>' and garbage:
            garbage = False
            continue

        if char == '{' and not garbage:
            depth += 1
            score += depth * 1
        elif char == '}' and depth > 0 and not garbage:
            depth -= 1

        if garbage:
            gbg_count += 1

        print 'Char is {}, garbage is {}, depth is {}'.format(char, garbage, depth)

    return score, gbg_count


def main():

    stream = get_input_rows(path)

    test = '{{<!!>},{<!!>},{<!!>},{<!!>}}'

    score, garbage = calculate_score(stream)
    print score, garbage

if __name__ == "__main__":
    main()

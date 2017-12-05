import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

def get_input_rows(fname, integer = False):

    with open(fname) as f:
        content = f.read().splitlines()

    if integer:
        content = map(int, content)

    return content

def read_instructions(instructions, complex = False):

    next = 0
    counter = 0

    while next >= 0 and next < len(instructions):

        #print 'Index is now {}'.format(next)

        step = instructions[next]

        if complex:
            if step < 3:
                instructions[next] += 1
            elif step >= 3:
                instructions[next] -= 1
        else:
            instructions[next] += 1

        counter += 1
        next += step

    return instructions, counter


def main():

    instructions = get_input_rows(path, integer = True)
    print instructions

    offsets, steps = read_instructions(instructions, complex = True)

    print offsets
    print steps

if __name__ == "__main__":
    main()

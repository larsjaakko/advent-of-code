import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

MAX_VALUE = 0

def get_input_rows(fname, integer = False):

    with open(fname) as f:
        content=[x.strip().split('\t') for x in f ]

    for i, row in enumerate(content):
        content[i] = row[0].split()
        content[i][2] = int(content[i][2])
        content[i][6] = int(content[i][6])

    if integer:
        content = map(int, content)

    return content

def process_instructions(instructions):

    registers = {}

    for i, row in enumerate(instructions):

        if row[0] not in registers:
            register = add_register(registers, row[0])
        if row[4] not in registers:
            register = add_register(registers, row[4])

        if evaluate_boolean(registers, row):
            registers = execute(registers, row)

    return registers



def evaluate_boolean(registers, row):

    if row[5] == '==':
        return registers[row[4]] == row[6]
    elif row[5] == '>':
        return registers[row[4]] > row[6]
    elif row[5] == '<':
        return registers[row[4]] < row[6]
    elif row[5] == '<=':
        return registers[row[4]] <= row[6]
    elif row[5] == '>=':
        return registers[row[4]] >= row[6]
    elif row[5] == '!=':
        return registers[row[4]] != row[6]
    else:
        print 'Got weird input! Can\'t evaluate operator {}'.format(row[5])


def execute(registers, row):

    if row[1] == 'inc':
        registers[row[0]] += row[2]
    elif row[1] == 'dec':
        registers[row[0]] -= row[2]

    global MAX_VALUE

    if registers[row[0]] >= MAX_VALUE:
        MAX_VALUE = registers[row[0]]

    return registers


def add_register(registers, new):

    registers.update({new: 0})

    return registers


def main():

    instructions = get_input_rows(path)

    registers = process_instructions(instructions)

    print max(registers.values())
    print registers

    print 'Highest value was {}'.format(MAX_VALUE)

if __name__ == "__main__":
    main()

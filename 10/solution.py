import os
import numpy as np

my_path = os.path.abspath(os.path.dirname(__file__))
test_path = path = os.path.join(my_path, "input_test.txt")
path = os.path.join(my_path, "input.txt")

def get_input_rows(fname, integer = False):

    with open(fname) as f:
        content = f.read()

    print content

    if integer:
        content = map(int, content)

    return content

def get_ascii_input(fname):

    with open(fname) as f:
        content = f.read().strip()

    content = [ord(c) for c in content]

    content.extend([17, 31, 73, 47, 23])

    return content

def sparse_hash(instructions):

    numbers = list(range(256))

    position = 0
    skip_size = 0

    iteration = 1

    while iteration <= 64:

        for length in instructions:

            if position + length <= len(numbers):

                temp = numbers[position:position+length]
                temp.reverse()

                for i, num in enumerate(temp):

                    numbers[position+i] = temp[i]

                position += (length + skip_size) % len(numbers)
                skip_size += 1

            elif position + length > len(numbers):

                remainder = position + length - len(numbers)

                temp = numbers[position:]
                temp.extend(numbers[:remainder])
                temp.reverse()

                for i, num in enumerate(temp):
                    if position + i < len(numbers):
                        numbers[position+i] = temp[i]
                    else:
                        numbers[position+i-len(numbers)] = temp[i]

                position += (length + skip_size) % len(numbers)

                skip_size += 1

            if position > len(numbers):
                position -= len(numbers)


            #print 'Iteration {}: {}'.format(iteration, numbers)
            #print 'Position is {} and skip_size is {}'.format(position, skip_size)

        iteration += 1

    return numbers

def dense_hash(hashed):

    dense = []

    for i in range(0,256,16):

        sparse = np.array(hashed[i:i+16])
        dense.append(np.bitwise_xor.reduce(sparse))

    return dense

def hexadecimal(dense):

    hex_string = ''

    for number in dense:

        hexed = format(number, 'x')
        if len(hexed) < 2:
            hexed = '0' + hexed
        hex_string += hexed

    return hex_string

def main():

    ascii_instructions = get_ascii_input(path)

    #instructions = get_input_rows(path, True)
    #print instructions

    hashed = sparse_hash(ascii_instructions)

    hashed = dense_hash(hashed)

    hexa = hexadecimal(hashed)
    print hexa

if __name__ == "__main__":
    main()

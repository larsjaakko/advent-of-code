import numpy as np
import math

def calculate_size(x):

    size = 1
    while size**2 < x:
        size += 2

    return size


def create_matrix(size, input = None, find_value = False):

    center = int(math.ceil(float(size)/2)) - 1
    print 'Center is set to: {}'.format(center)
    matrix = np.zeros((size, size), dtype=int)

    matrix[center, center] = 1

    col = center + 1
    row = center

    direction = 'r'
    counter = 2

    while counter <= size ** 2:

        if find_value:
            # Couldn't be bothered adding logic to avoid index errors for
            # edge or corner indices.
            # This will fail for very low inputs
            value = (matrix[row, col+1]
                     + matrix[row, col-1]
                     + matrix[row-1, col]
                     + matrix[row+1, col]
                     + matrix[row-1, col-1]
                     + matrix[row-1, col+1]
                     + matrix[row+1, col-1]
                     + matrix[row+1, col+1])

            if value > input:
                print "The first value exceeding {} is {}".format(input, value)
                return

        matrix[row, col] = counter

        if not find_value:
            print 'Wrote number {} to index [{},{}]'.format(counter, row, col)
        else:
            print 'Wrote number {} to index [{},{}]'.format(value, row, col)
            
        if direction == 'r' and not matrix[row - 1, col] == 0:
            col += 1
            counter += 1
            continue
        elif direction == 'r' and matrix[row - 1, col] == 0:
            row -= 1
            counter += 1
            direction = 'u'
            continue

        elif direction == 'u' and not matrix[row, col - 1] == 0:
            row -= 1
            counter += 1
            continue
        elif direction == 'u' and matrix[row, col - 1] == 0:
            col -= 1
            counter += 1
            direction = 'l'
            continue

        elif direction == 'l' and not matrix[row + 1, col] == 0:
            col -= 1
            counter += 1
            continue
        elif direction == 'l' and matrix[row + 1, col] == 0:
            row += 1
            counter += 1
            direction = 'd'
            continue

        elif direction == 'd' and not matrix[row, col + 1] == 0:
            row += 1
            counter += 1
            continue
        elif direction == 'd' and matrix[row, col + 1] == 0:
            col += 1
            counter += 1
            direction = 'r'
            continue


    return matrix

def find_distance(matrix, value, size):

    center = int(math.ceil(float(size)/2)) - 1

    row, col = np.where(matrix == value)

    return abs(row - center) + abs(col - center)

def main():

    input = 361527

    size = calculate_size(input)

    #matrix = create_matrix(size)

    create_matrix(size, input, True)

    #print matrix

    #print find_distance(matrix, input, size)


if __name__ == "__main__":
    main()

import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

def get_input_rows(fname, integer = False):

    with open(fname) as f:
        content = f.read().split()

    if integer:
        content = map(int, content)

    return content

def redistribute(blocks):

    record = {}
    done = False
    iteration = 1
    occurence = 0

    while not done:

        # Find the lowest index with the highest number
        idx = blocks.index(max(blocks))
        next_idx = idx + 1
        block = max(blocks)
        blocks[idx] = 0


        # Redistributing the values
        while block > 0:
            if next_idx < len(blocks):
                blocks[next_idx] += 1
                next_idx += 1
                block -= 1
            else:
                next_idx = 0

        # Add tuple of the solution to record
        if tuple(blocks) not in record.values():
            print 'Adding tuple {} to record'.format(tuple(blocks))
            record.update( {iteration: tuple(blocks)})
            iteration += 1
        else:
            print 'Tuple {} is a duple!'.format(tuple(blocks))
            cycle = iteration - record.keys()[record.values().index(tuple(blocks))]
            done = True

    return iteration, blocks, cycle




def main():

    blocks = get_input_rows(path, integer = True)
    print blocks

    iteration, blocks, cycle = redistribute(blocks)
    print cycle

if __name__ == "__main__":
    main()

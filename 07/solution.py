import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

def get_input_rows(fname):

    with open(fname,'r') as f:
        content=[x.strip().split('\t') for x in f ]

    for i, row in enumerate(content):
        content[i] = row[0].split()
        content[i][1] = content[i][1].replace('(', '')
        content[i][1] = content[i][1].replace(')', '')
        content[i][1] = int(content[i][1])

    for i, row in enumerate(content):
        for j, word in enumerate(row):
            try:
                row[j] = row[j].replace(',', '')
            except:
                pass

    return content

def search_bottom(towers, current_btm):

    new_btm = None

    for i, row in enumerate(towers):
        if current_btm in row[2:]:
            new_btm = row[0]
            return search_bottom(towers, new_btm)

    if new_btm is None:
        return current_btm

def find_unbalanced(towers, current_btm, previous_weights = None):

    print '\nChecking program called {}'.format(current_btm)

    weights = {}

    for i, row in enumerate(towers):
        if row[0] == current_btm and len(row) > 2:
            for j in range(3, len(row)):
                weights.update({row[j]: sum_weights(towers, row[j], first = True)})
        elif row[0] == current_btm and len(row) == 2:
            print 'Found the top at {}, sending back the weights: {}'.format(current_btm, previous_weights)
            return previous_weights

    counts = {}
    for key, value in weights.iteritems():
        if value in counts:
            counts[value] += 1
        else:
            counts.update({value: 1})

    print 'Weights at program {} are: {}'.format(current_btm, weights)

    for key, values in weights.iteritems():
        if len(weights) > 2 and counts[values] == 1:
            return find_unbalanced(towers, key, weights)
        elif len(weights) == 2:
            return 'Found level with two programs!'
        elif len(weights) < 1:
            return 'Something went wrong, number of programs is {} and the weights are {} and the counts are {}'.format(len(weights), weights, counts)

    
    return 'Rest is balanced. Unbalanced program is {}'.format(current_btm)


def sum_weights(towers, current_program, first = False):

    level_weight = 0

    for i, row in enumerate(towers):
        if row[0] == current_program and len(row) > 2:
            level_weight += row[1]
            for j in range(3, len(row)):
                level_weight += sum_weights(towers, row[j])
        if row[0] == current_program and len(row) == 2:
            return row[1]

    return level_weight


def main():

    towers = get_input_rows(path)
    #print towers

    bottom = search_bottom(towers, towers[0][0])
    print 'Bottom program is {}'.format(bottom)

    print '\nSearching for unbalanced program!'

    unbalanced = find_unbalanced(towers, bottom)
    print unbalanced

if __name__ == "__main__":
    main()

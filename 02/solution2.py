import os.path
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

with open(path,'r') as f:
    content=[x.strip().split('\t') for x in f]

for i, row in enumerate(content):
    content[i] = map(int, content[i])

divisible = []

for i, row in enumerate(content):
    for j, numerator in enumerate(row):
        for k, denominator in enumerate(row):

            if j != k and numerator >= denominator and numerator % denominator == 0:
                divisible.append(numerator / denominator)

        continue
    continue

print divisible
print sum(divisible)

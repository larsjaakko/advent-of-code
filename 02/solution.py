import os.path
import csv

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "input.txt")

with open(path,'r') as f:
    content=[x.strip().split('\t') for x in f]

for i, row in enumerate(content):
    content[i] = map(int, content[i])

checksums = []

for i, row in enumerate(content):
     checksums.append(max(content[i]) - min(content[i]))

print checksums
print sum(checksums)

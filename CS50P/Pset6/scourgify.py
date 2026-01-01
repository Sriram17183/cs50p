import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

inputfile = sys.argv[1]
outputfile = sys.argv[2]

students = []

# Read from input CSV
with open(inputfile) as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        last, first = row['name'].split(', ')
        print(last,first)
        students.append({'first': first,'last': last,'house': row['house']})

# Write to output CSV
with open(outputfile, 'w') as file2:
    fieldnames = ['first', 'last', 'house']
    writer = csv.DictWriter(file2, fieldnames=fieldnames)
    writer.writeheader()
    for student in students:
        writer.writerow(student)

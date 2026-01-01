import sys
import csv
from tabulate import tabulate
if len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")

y = sys.argv[1]

if not y.endswith(".csv"):
    sys.exit("Not a csv file")

file = sys.argv[1]

with open(file) as d:
    read=csv.reader(d)
    read=list(read)
    headers=read[0]
    read.remove(read[0])
    print(tabulate(read,headers,tablefmt="grid"))

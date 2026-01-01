import sys

if len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")

y = sys.argv[1]

if not y.endswith(".py"):
    sys.exit("Not a python file")

file = sys.argv[1]

k = 0
with open(file) as d:
    for line in d:
        stripped = line.strip()
        if stripped == "" or stripped.startswith("#"):
            continue
        k=k+1
print(k)




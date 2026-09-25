fname = input("Enter file name: ")
fh = open(fname)

count = 0
for line in fh:

    if not line.startswith('count'):
        continue

    
    count = count + 1
    address = line.split()[1]
    print(address)

print("There were", count, "lines in the file with From as the first word")

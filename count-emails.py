name = input("Enter file:")
fh =open(name)
counts = dict()

for line in fh:
    if not line.startswith("From "):
        continue

    words = line.split()
    email = words[1]
    
    

    counts[email] = counts.get(email, 0) + 1

largest_count = None
largest_email = None

for email,count in counts.items():
    if largest_count is None or count > largest_count:
        largest_email = email
        largest_count = count

print (largest_email, largest_count)
    
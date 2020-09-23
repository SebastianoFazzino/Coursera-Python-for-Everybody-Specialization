import re
file = open("file.txt")
total = 0
for line in file:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    for i in numbers:
        total = total + int(i)
    
print(total)
List = list()
Dict = dict()
openfile = open('Assignment.txt')
for line in openfile:
    if not line.startswith("From ") : continue
    result = line.find(':')
    result1 = line[result - 2 : result]
    Dict[result1] = Dict.get(result1, 0) + 1

for key,value in sorted(Dict.items()):
    print(key,value)   
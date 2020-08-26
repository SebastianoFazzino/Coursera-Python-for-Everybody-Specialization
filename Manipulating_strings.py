#Uppers and Lowers:
greet = 'Hello, Bob'
print("Upper Cases: ",greet.upper()," Lower Cases: ",greet.lower())



#search and replace:
greets = 'Hello, Bob'
Replace = greets.replace('Bob','Jane')
print(Replace)

Replace2 = greets.replace('o','a')
print(Replace2)


#stripping whitespaces:
greet1 = '    Hello, Bob   '
print(greet1.lstrip()) #left
print(greet1.rstrip()) #right
print(greet1.strip())  #both


#prefixes:
line = 'Please have a nice day!'
print(line.startswith('Please'))
print(line.startswith('p'))


#parsing and extracting:
email = 'sebastianofazzino@gmail.com - Sebastiano'
at_position = email.find('@')
print(at_position) #17
space_position = email.find(' ')
print(space_position) #27
host = email[at_position + 1 : space_position]
print(host)


#1st week assignment
text = "X-DSPAM-Confidence:    0.8475";
sliced = text.find('    ')
slice2 = text.find('5')
result = text[sliced + 1 : slice2 + 1]
print(float(result))

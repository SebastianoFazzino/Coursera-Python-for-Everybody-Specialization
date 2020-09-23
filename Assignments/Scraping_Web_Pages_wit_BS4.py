import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = ('http://py4e-data.dr-chuck.net/comments_901169.html')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
total = 0
tags  = soup('span')
for tag in tags:
    numbers = tag.contents
    for number in numbers:
        total = total + int(number)
        
print(total)
    
   
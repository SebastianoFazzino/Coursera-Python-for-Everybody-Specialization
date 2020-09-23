import urllib
import xml.etree.ElementTree as ET

count = 0
Sum = 0

url = input ("Enter location:")
URL = urllib.request.urlopen(url)
data = URL.read()


tree = ET.fromstring(data)
Comments = tree.findall('comments/comment')

for item in Comments:
    Count = int(item.find('count').text)
    count = count + 1
    Sum = Sum + Count
    
print('Count:', count)   
print('Sum:', Sum)

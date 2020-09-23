import urllib.error, urllib.request, urllib.parse
import json

site = 'http://py4e-data.dr-chuck.net/json?' 
location = input('Enter location: ')
url = location + urllib.parse.urlencode({'address': location, 'key' : 42})

print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
print(json.dumps(js, indent = 4)) 
print('Place id', js['results'][0]['place_id'])

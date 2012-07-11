import json
import re
import urllib2

url='http://api.ravelry.com/projects/radioaction/progress.json?key=b1d7f00b28eeb4a172a134d4ce6fc325f3c44bc2&notes=true&status=in-progress+hibernating+finished+frogged'
data = json.load(urllib2.urlopen(url)) 
r = re.compile('sock', flags=re.IGNORECASE)
second_socks = {}
for p in data['projects']:
	name = p['name']
	progress = p['progress']
	status = p['status']
	if r.search(name) and progress >=50 and progress < 100 and status == 'in-progress' :
		second_socks[name] = progress
		print name + ' : ' + p['status'] + ' : ' + str(progress)

print second_socks
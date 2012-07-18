import json
import re
import urllib2


def fetch_projects(url):
    projects = json.load(urllib2.urlopen(url)) 
    return projects
def secondsocks(projects):
    second_socks = {}
    r = re.compile('sock', flags=re.IGNORECASE)
    for p in projects['projects']:
        name = p['name']
        progress = p['progress']
        status = p['status']
        if r.search(name) and progress >=50 and progress < 100 and status == 'in-progress' :
            second_socks[name] = p
    return second_socks

if __name__ == "__main__":
    url='http://api.ravelry.com/projects/radioaction/progress.json?key=b1d7f00b28eeb4a172a134d4ce6fc325f3c44bc2&notes=true&status=in-progress+hibernating+finished+frogged'
    s = secondsocks(fetch_projects(url))
    print s



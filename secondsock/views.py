from django.http import HttpResponse
import projects

def hello(request):
    return HttpResponse("Hello world")

def secondsock(request):
    url='http://api.ravelry.com/projects/radioaction/progress.json?key=b1d7f00b28eeb4a172a134d4ce6fc325f3c44bc2&notes=true&status=in-progress+hibernating+finished+frogged'
    s = projects.secondsocks(projects.fetch_projects(url))
    return HttpResponse(s)

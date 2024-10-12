from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseNotFound
from django.template import loader
import mimetypes
from django.conf import settings



# Create your views here.

# handles request 

def getFileType(filePath):
    fileType = mimetypes.guess_type(filePath)
    return fileType


def indexHandler(request): 
    template = str(loader.get_template('index.html'))
    return HttpResponse(render(request,template))


def textHandler(request):
    fileType = getFileType(request.path)
    if fileType in ['js', 'css', 'html']:
        template = str(loader.get_template(request.path))

        response = HttpResponse()

        response['content'] = str(loader.get_template(request.path))
        response['Content-Length'] = len(response.content)
        response['content_type'] = fileType
        response['X-Content-Type-Options'] = "nosniff"
        
        #Content-Length
        #Content-Type
        #X-Content-Type-Options: nosniff
        #HTTP/1.1 200 OK

    else:
        return HttpResponseNotFound("HTTP/1.1 404 Not Found OK")
            
# def imgHandler(request):

# Create your views here
#views are just the handler for shit that will be pass into urls.py


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
import mimetypes
from pathlib import Path
from urllib.parse import quote



def getFileType(filePath):
    return mimetypes.guess_type(filePath)[0]  

def indexHandler(request):
    return render(request, 'index.html')

def fileHandler(request, fileName): # can handle img and text 
    sanitizedfileName = quote(fileName) # get a clean full file path 
    path = Path(settings.STATIC_ROOT) / sanitizedfileName

    allowedType = {'.css', '.html', '.js', '.png', '.jpg', '.jpeg', '.gif', '.mp3', '.mp4', '.xml', '.json', '.pdf'} # can add more, 

    if not path.suffix.lower() in allowedType: # to deal with user uploads 
        return HttpResponseNotFound("404 - File type not allowed")
    
    #deal with /../ attacks 
    rootPath = Path(settings.STATIC_ROOT).resolve() #.resolve get absolute path 
    if not path.resolve().is_relative_to(rootPath):
        return HttpResponseNotFound("404 - Invalid file path")
    
    if path.exists() and path.is_file(): # make sure its not a directory 
        contentType = getFileType(path)
        
        try:
            with open(path, 'rb') as file:
                content = file.read()

            response = HttpResponse(content, content_type=contentType)
            response['X-Content-Type-Options'] = "nosniff"
            response['Content-Length'] = str(len(content))

            print(response)
        
            return response
        
        except OSError as e: # catch most of em, like FileNotFoundError  
            return HttpResponseNotFound(f"404 - Error reading file: {e}")
            #return render(request, '404.html', status=404) when make 404 pages 
        
    else:
        return HttpResponseNotFound("404 Not Found")
    
def addCookies(response, cookies): # add all cookies from the give dic to the response
    for cookieName, cookieValue in cookies.items():
        response.set_cookie(cookieName, cookieValue)
    return response

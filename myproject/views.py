from django.shortcuts import render
#from .custom_logger import logger
import logging
#log = logger(False, True, __name__)

log = logging.getLogger(__name__)

def homepage(request):
    #return HttpResponse("Home Page")
    log.debug("Homepage")
    return render(request, 'home.html')

def aboutpage(request):
    #return HttpResponse("About Page")
    log.info("About")
    return render(request, 'about.html')
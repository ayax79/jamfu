from django.template.context import RequestContext
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('main/index.html',
                              context_instance=RequestContext(request))

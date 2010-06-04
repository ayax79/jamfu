from django.shortcuts import render_to_response
from django.conf import settings
from django.template.context import RequestContext

def index(request):
    return render_to_response('facebook/index.html', {'facebook_info': settings.FACEBOOK_INFO},
                       context_instance=RequestContext(request))


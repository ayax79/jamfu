from django.shortcuts import render_to_response
from django.conf import settings
from django.template.context import RequestContext

def index(request):
    return render_to_response('facebook/index.html', {'facebook_info': facebook_info()},
                              context_instance=RequestContext(request))

def facebook_info():
    return {
    'key': settings.FACEBOOK_API_KEY,
    'secret': settings.FACEBOOK_SECRET_KEY,
    'app_id': settings.FACEBOOK_APP_ID,
    }

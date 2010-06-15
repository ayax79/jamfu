from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, settings

def index(request):
    return render_to_response('main/index.html',
                              context_instance=RequestContext(request))

def login(request):
    return HttpResponseRedirect(_build_redirect_url())
#    return render_to_response('main/login.html',
#                              context_instance=RequestContext(request))

def login_submit(request):
    return HttpResponseRedirect(_build_redirect_url())

def _build_redirect_url():
    url = "https://graph.facebook.com/oauth/authorize?client_id="
    url += settings.FACEBOOK_APP_ID
    url += "&redirect_uri="
    url += settings.LOGIN_REDIRECT
    url += "&scope=user_photos,user_videos,publish_stream"
    return url



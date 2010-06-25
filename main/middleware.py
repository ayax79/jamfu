from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect

class RequireLoginMiddleware(object):
    """
    Require Login middleware. If enabled, each Django-powered page will
    require authentication.

    If an anonymous user requests a page, he/she is redirected to the login
    page set by REQUIRE_LOGIN_PATH or /accounts/login/ by default.
    """

    def __init__(self):
        self.require_login_path = settings.REQUIRE_LOGIN_PATH 
        self.exclusions = settings.AUTH_EXCLUSION_PATHS

    def is_exclude_path(self, request):
        path = request.path
        for ex in self.exclusions:
            if path.find(ex) == -1:
                return True
        return False

    def is_ignored(self, request):
        return ((request.path != self.require_login_path and not
                request.user.is_anonymous) or
                self.is_exclude_path(request))

    def process_request(self, request):
        if self.is_ignored(request):
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('%s?next=%s' % (self.require_login_path, request.path))

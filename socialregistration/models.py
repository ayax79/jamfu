from django.db import models

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class BaseSiteable(models.Model):
    site_id = models.IntegerField(default=Site.objects.get_current)

    def site(self):
        return Site.objects.get(pk=self.site_id)

    @staticmethod
    def current_site_id():
        current_site = Site.objects.get_current()
        if (current_site):
            return current_site.id


class BaseExternalProfile(BaseSiteable):
    user_id = models.IntegerField()

    def user(self):
        return User.objects.get(pk=self.user_id)


class FacebookProfile(BaseSiteable):

    uid = models.CharField(max_length=255, blank=False, null=False)
    
    def __unicode__(self):
        return u'%s: %s' % (self.user, self.uid)
    
    def authenticate(self):
        return authenticate(uid=self.uid)

class TwitterProfile(BaseExternalProfile):
    twitter_id = models.PositiveIntegerField()
    
    def __unicode__(self):
        return u'%s: %s' % (self.user, self.twitter_id)
    
    def authenticate(self):
        return authenticate(twitter_id=self.twitter_id)

class OpenIDProfile(BaseExternalProfile):
    identity = models.TextField()
    
    def __unicode__(self):
        return u'OpenID Profile for %s, via provider %s' % (self.user, self.identity)

    def authenticate(self):
        return authenticate(identity=self.identity)

class OpenIDStore(BaseSiteable):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()

    def __unicode__(self):
        return u'OpenID Store %s for %s' % (self.server_url, self.site)

    def site(self):
        return Site.objects.get(pk=self.site_id)

class OpenIDNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'OpenID Nonce for %s' % self.server_url

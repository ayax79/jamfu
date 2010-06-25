"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from main.middleware import RequireLoginMiddleware
from mock import Mock

class RequireLoginMiddlewareTest(TestCase):

    def setUp(self):
        self.mw = RequireLoginMiddleware()
        self.req = Mock()
        self.user = Mock()

    def test_excluded_false(self):
        """
        Confirms that /blah is not an excluded path
        """
        self.req.path = "/blah"
        self.assertFalse(self.mw.is_exclude_path(self.req))

    def test_excluded_facebook(self):
        """
        Confirms that url under /facebook/ is excluded
        """
        self.req.path = "/facebook/sdlfkjdsf"
        self.assertTrue(self.mw.is_exclude_path(self.req))
    
    def test_is_ignored_login_path(self):
        """
        Tests that "/login" is ignored
        """
        self.req.path = "/login"
        self.assertTrue(self.mw.is_ignored(self.req))

    def test_is_ignored_fail_1(self):
        """
        Tests that "/blah" is not ignore for anonymous
        """
        self.req.path = "/blah"
        self.user.is_anonymous = True
        self.req.user = self.user
        mw = RequireLoginMiddleware()
        self.assertFalse(self.mw.is_ignored(self.req))


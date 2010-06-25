"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from main.middleware import RequireLoginMiddleware
from mock import Mock

class MiddlewareTest(TestCase):
    
    def test_is_ignored_login_path(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        req = Mock()
        req.path = "/login"

        mw = RequireLoginMiddleware()
        self.assertTrue(mw.is_ignored(req))

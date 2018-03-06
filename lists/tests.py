# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page #will be written by ourselves

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/') # passing URL we want to test
        self.assertTemplateUsed(response, 'wrong.html') 

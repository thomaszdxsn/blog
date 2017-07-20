#!/usr/bin/env python3
from django.test import TestCase


class TestPostViews(TestCase):

    def test_home_page_content(self):
        response = self.client.get("http://localhost:8000")
        self.assertIn("博客首页", response.content.decode())


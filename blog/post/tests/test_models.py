#!/usr/bin/env python3
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from ..models import Post


class TestPostModel(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username="example", email="example@qq.com")
        super().setUpClass()

    def test_slug_can_auto_generated(self):
        p = Post.objects.create(title="你好", author=self.user,
                                 content="test")
        self.assertEqual(p.slug, "ni-hao")

    def test_generated_slug_maxium_length_less_than_100(self):
        p = Post.objects.create(title="如果我是DJ，你会爱我吗？你会爱我吗？你会爱我吗？"
                                      "你会爱我吗？你会爱我吗？你会爱我吗？你会爱我吗?",
                                author=self.user, content="test")
        self.assertTrue(len(p.slug) <= 100)

    def test_generated_slug_not_be_duplicate(self):
        p1 = Post.objects.create(title="你好", author=self.user,
                                 content="test")
        p2 = Post.objects.create(title="你好", author=self.user,
                                 content="test")
        self.assertNotEqual(p1.slug, p2.slug)
        self.assertTrue(p2.slug.endswith("2"))

    def test_generated_slug_maxinum_length_but_duplicate_also_endswith_ordered_num(self):
        p1 = Post.objects.create(title="如果我是DJ，你会爱我吗？你会爱我吗？你会爱我吗？"
                                       "你会爱我吗？你会爱我吗？你会爱我吗？你会爱我吗?",
                                author=self.user, content="test")
        p2 = Post.objects.create(title="如果我是DJ，你会爱我吗？你会爱我吗？你会爱我吗？"
                                       "你会爱我吗？你会爱我吗？你会爱我吗？你会爱我吗?",
                                author=self.user, content="test")
        self.assertTrue(len(p2.slug) <= 100)
        self.assertTrue(p2.slug.endswith("2"))

    def test_published_manager_only_return_time_before_now(self):
        now = timezone.now()
        p1 = Post.objects.create(title="test1", author=self.user,
                                 content="test", publish_time=now)
        p2 = Post.objects.create(title="test2", author=self.user,content="test",
                                 publish_time=now.replace(day=now.day + 1))
        posts = Post.published.all()
        self.assertEqual(posts.count(), 1)
        self.assertEqual(posts[0], p1)

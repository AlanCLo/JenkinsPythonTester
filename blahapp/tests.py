# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from blahapp.models import Human, Cat
from django.utils import timezone
from django.core.urlresolvers import reverse
from blahapp.forms import CatForm


# Create your tests here.


class ModelTestCase(TestCase):
	def setUp(self):
		h = Human.objects.create(name="Alan")
		Cat.objects.create(name="lion", owner=h)
		Cat.objects.create(name="asdf", owner=h)

	def test_created(self):
		self.assertEqual(len(Human.objects.all()), 1)
		self.assertEqual(len(Cat.objects.all()), 2)

	#def test_tostring_for_coverage(self):
	#	self.assertEqual(str(Human.objects.all()[0]), "Human: Alan")
	#	self.assertEqual(str(Cat.objects.all()[0]), "Cat: lion")


class CatViewTestCase(TestCase):
	def setUp(self):
		h = Human.objects.create(name="Alan")
		Cat.objects.create(name="lion", owner=h)

	def test_cat_list_view(self):
		url = reverse("cat_list")
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)
		self.assertIn("lion", resp.content)



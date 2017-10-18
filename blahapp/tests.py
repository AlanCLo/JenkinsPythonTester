# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from blahapp.models import Human, Cat

# Create your tests here.


class ModelTestCase(TestCase):
	def setUp(self):
		h = Human.objects.create(name="Alan")
		Cat.objects.create(name="lion", owner=h)
		Cat.objects.create(name="asdf", owner=h)

	def test_created(self):
		self.assertEqual(len(Human.objects.all()), 1)
		self.assertEqual(len(Cat.objects.all()), 2)



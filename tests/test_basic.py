#!/usr/bin/python

import unittest
from base import BaseTestCase

class AppTestCase(BaseTestCase):
	def test_index(self):
		response = self.client.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)

	def test_page_loads(self):
		response = self.client.get('/')
		self.assertIn(b'Your links', response.data)


if __name__ == '__main__':
	unittest.main()


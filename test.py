#!/usr/bin/python
# this test runs against dev db

from coreapp import app
import unittest


class SimpleTestCase(unittest.TestCase):
	def test_index(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertEqual(response.status_code, 200)


	def test_page_loads(self):
		tester = app.test_client(self)
		response = tester.get('/', content_type='html/text')
		self.assertIn(b'Your links', response.data)


if __name__ == '__main__':
	unittest.main()


import unittest

from pynotifier import Notification


class TestNotification(unittest.TestCase):

	def setUp(self) -> None:
		self.notification = Notification(
			title='Hello',
			message='World'
		)

	def test_title(self):
		self.assertEqual(self.notification.title, 'Hello')

	def test_message(self):
		self.assertEqual(self.notification.message, 'World')

	def test_config(self):
		self.assertEqual(self.notification.config, {
			'title': 'Hello',
			'message': 'World'
		})

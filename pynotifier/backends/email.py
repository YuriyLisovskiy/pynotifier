"""
This file is a part of py-notifier project.

Copyright (c) 2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""
from pynotifier.notification import Notification


class EmailBackend:
	"""
	Email notification backend.
	"""

	IDENTIFIER = 'pynotifier.backends.email'

	def notify(self, notification: Notification):
		"""Send the notification using config from Notification object."""
		raise NotImplementedError

"""
This file is a part of py-notifier project.

Copyright (c) 2022 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from ..notification import Notification


class NotificationBackend:
	"""
	Base class for notification backends.

	Child classes can provide some pre- or post-processing
	of the notification it sends.
	"""

	IDENTIFIER = None

	def notify(self, notification: Notification):
		"""Sends the notification using config from Notification object."""
		raise NotImplementedError

	@property
	def identifier(self):
		"""
		Returns backend identifier, usually it has package notation, i.e.
		pynotifier.backends.my_backend
		"""
		return self.IDENTIFIER

"""
This file is a part of py-notifier project.

Copyright (c) 2022-2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from pynotifier.notification import Notification


class NotificationBackend:
	"""
	Base class for notification backends.

	Child classes can provide some pre- or post-processing
	of the notification it sends.
	"""

	IDENTIFIER = None

	def notify(self, notification: Notification):
		"""Send the notification using config from Notification object."""
		raise NotImplemented

	@property
	def identifier(self):
		"""
		Backend identifier.

		Usually it has package notation, i.e. pynotifier.backends.my_backend.
		"""
		if self.IDENTIFIER is None:
			raise NotImplemented

		return self.IDENTIFIER

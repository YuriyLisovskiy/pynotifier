"""
This file is a part of py-notifier project.

Copyright (c) 2022 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from .backends import NotificationBackend
from .notification import Notification


class NotificationClient:
	"""Holds backends to notify and sends the notification using them."""

	def __init__(self):
		"""Initialize an empty backends list."""
		self._backends = []

	def register_backend(self, backend: NotificationBackend):
		"""Append the provided backend."""
		self._backends.append(backend)

	def notify_all(self, notification: Notification):
		"""Send the notification to all backends."""
		for backend in self._backends:
			backend.notify(notification)

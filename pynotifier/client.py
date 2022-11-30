# Copyright (c) 2022 Yuriy Lisovskiy
#
# Distributed under the MIT licence, see the accompanying file LICENSE.

from .backends import NotificationBackend
from .notification import Notification


class NotificationClient:

	def __init__(self):
		self._backends = []

	def register_backend(self, backend: NotificationBackend):
		self._backends.append(backend)

	def notify_all(self, notification: Notification):
		for backend in self._backends:
			backend.notify(notification)

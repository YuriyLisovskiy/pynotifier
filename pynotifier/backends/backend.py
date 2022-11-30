# Copyright (c) 2022 Yuriy Lisovskiy
#
# Distributed under the MIT licence, see the accompanying file LICENSE.

from ..notification import Notification


class NotificationBackend:
	IDENTIFIER = None

	def notify(self, notification: Notification):
		raise NotImplementedError

	@property
	def identifier(self):
		return self.IDENTIFIER

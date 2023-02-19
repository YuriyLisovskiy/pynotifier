"""
This file is a part of py-notifier project.

Copyright (c) 2022-2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from pynotifier.notification import Notification
from pynotifier.utils import assert_system

from ..backend import NotificationBackend

assert_system('windows')

try:
	import win_toaster
except ImportError:
	raise ImportError("notifications are not supported, can't import win_toaster")


class WindowsBackend(NotificationBackend):
	"""
	Desktop notification backend for windows.

	Current implementation uses 3rd party module - "WinToaster" to send notifications.
	"""

	IDENTIFIER = "pynotifier.backends.platform.windows"

	def notify(self, notification: Notification):
		"""
		Send notification on windows with WinToaster.

		'title' - a title of notification
		'message' - more info about the notification
		'duration' - the duration, in seconds, for the notification to appear on screen
		'icon_path' - a filename of the icon to display
		'sound' - a filename of custom sound in .wav format
		"""
		win_toaster.create_toast(
			threaded=True,
			title=notification.title,
			msg=notification.message,
			duration=int(notification.config.get('duration', '5')),
			icon_path=notification.config.get('icon_path', None),
			sound_path=notification.config.get('sound', None)
		).display()


Backend = WindowsBackend

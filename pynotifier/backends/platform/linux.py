"""
This file is a part of py-notifier project.

Copyright (c) 2022-2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

import shutil
import subprocess

from pynotifier.notification import Notification
from pynotifier.utils import assert_system

from ..backend import NotificationBackend

assert_system('linux')


class LinuxBackend(NotificationBackend):
	"""
	Desktop notification backend for linux.

	Current implementation uses libnotify-bin tool to send notifications.
	"""

	IDENTIFIER = "pynotifier.backends.platform.linux"

	def notify(self, notification: Notification):
		"""
		Send notification on linux with notify-send.

		'title' - a title of notification
		'message' - more info about the notification
		'duration' - the duration, in seconds, for the notification to appear on screen
					(Ubuntu's Notify OSD and GNOME Shell both ignore this parameter.)
		'urgency' - the urgency level (low, normal, critical)
		'icon_path' - an icon filename or stock icon to display
		'app_name' - the app name for the notification
					(Works on Arch Linux)
		"""
		notify_send = shutil.which("notify-send")
		if notify_send is None:
			raise SystemError(
				"""Please install libnotify-bin.
For Ubuntu run the following command in terminal:
	apt-get install libnotify-bin"""
			)

		command = [
			notify_send,
			"{}".format(notification.title),
			"{}".format(notification.message),
			"-t",
			"{}".format(int(notification.config.get('duration', '5')) * 1000),
		]
		urgency = notification.config.get('urgency', None)
		if urgency is not None:
			command += ["-u", urgency]

		icon_path = notification.config.get('icon_path', None)
		if icon_path is not None:
			command += ["-i", icon_path]

		app_name = notification.config.get('app_name', None)
		if app_name is not None:
			command += ["-a", str(app_name)]

		subprocess.Popen(command, shell=False)


Backend = LinuxBackend

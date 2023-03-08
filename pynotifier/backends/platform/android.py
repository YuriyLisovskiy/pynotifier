"""
This file is a part of py-notifier project.

Copyright (c) 2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

import shutil
import subprocess

from pynotifier.notification import Notification
from pynotifier.utils import assert_system

from ..backend import NotificationBackend

assert_system('android')


class AndroidTermuxBackend(NotificationBackend):
	"""
	Notifications backend for Android Termux.

	Current implementation uses termux-notification and termux-toast tool to send notifications.
	"""

	IDENTIFIER = "pynotifier.backends.platform.android"

	def notify(self, notification: Notification):
		"""
		Send notification on Android with termux-notification or termux-toast.

		'title' - a title of notification
		'message' - more info about the notification
		TODO: add available params of notification and it's config...
		"""
		command = []
		if notification.config.get('toast', False):
			command = [
				self._get_cli_app('termux-toast'),
				"\"{}: {}\"".format(notification.title, notification.message),
			]
			# TODO: Append command args...
		else:
			command = [
				self._get_cli_app('termux-notification'),
				"--title", "\"{}\"".format(notification.title),
				"--content", "\"{}\"".format(notification.message),
			]
			# TODO: Append command args...

		subprocess.Popen(command, shell=False)

	@staticmethod
	def _get_cli_app(name: str):
		app = shutil.which(name)
		if app is None:
			raise SystemError(
				f"""Please install Termux:API which includes the {name} app.
Visit the https://f-droid.org/en/packages/com.termux.api/ website to install the Termux:API"""
			)

		return app


Backend = AndroidTermuxBackend

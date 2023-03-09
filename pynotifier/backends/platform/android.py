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

TOAST_POSITION_TOP = 'top'
TOAST_POSITION_MIDDLE = 'middle'
TOAST_POSITION_BOTTOM = 'bottom'

_AVAILABLE_TOAST_POSITIONS = [TOAST_POSITION_MIDDLE, TOAST_POSITION_MIDDLE, TOAST_POSITION_BOTTOM]


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

		Termux Toast config
		'termux_toast':
			'bg_color' - the background color (default: gray) (standard name, "#FF0000" or "#FFFF0000")
			'text_color' - the text color (default: white) (standard name, "#FF0000" or "#FFFF0000")
			'position' - the position of the toast [top, middle, bottom] (default: middle)
			'show_short' - only show the toast for a short time

		Termux Notification config:
		'termux':
			'' -
		"""
		if notification.config.get('toast', False):
			command = [
				self._get_cli_app('termux-toast'),
				"\"{}: {}\"".format(notification.title, notification.message),
			] + self._build_toast_opts(notification.config.get('termux_toast', dict()))
		else:
			command = [
				self._get_cli_app('termux-notification'),
				"--title", "\"{}\"".format(notification.title),
				"--content", "\"{}\"".format(notification.message),
			] + self._build_notification_opts(notification.config.get('termux', dict()))

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

	@staticmethod
	def _build_toast_opts(config: dict):
		opts = [
			'-b', config.get('bg_color', 'gray'),
			'-c', config.get('text_color', 'white')
		]

		show_short = _validate_opt_or_default(config.get('show_short', 'true'), ['true', 'false'], 'false')
		opts += ['-s', show_short]

		position = _validate_opt_or_default(
			config.get('position', TOAST_POSITION_MIDDLE),
			_AVAILABLE_TOAST_POSITIONS,
			TOAST_POSITION_MIDDLE
		)
		opts += ['-g', position]

		return opts

	@staticmethod
	def _build_notification_opts(config: dict):
		opts = []
		#TODO: add opts from doc: https://wiki.termux.com/wiki/Termux-notification

		return opts


def _validate_opt_or_default(opt: str, available_values: list, default: object):
	if opt not in available_values:
		return default

	return opt


Backend = AndroidTermuxBackend

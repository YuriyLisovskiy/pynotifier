"""
This file is a part of py-notifier project.

Copyright (c) 2022-2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

import subprocess
from os import walk

from pynotifier.notification import Notification
from pynotifier.utils import assert_system

from ..backend import NotificationBackend

assert_system('darwin')


def _load_sounds(p: str):
	try:
		return set(next(walk(p), (None, None, []))[2])
	except FileNotFoundError as exc:
		print(exc)
		return set()


_sounds_locations = [
	'/System/Library/Sounds',
	'~/Library/Sounds'
]

sounds = set()
for sounds_location in _sounds_locations:
	sounds = sounds.union(_load_sounds(sounds_location))

sounds = tuple(sounds)


class DarwinBackend(NotificationBackend):
	"""
	Desktop notification backend for macOS.

	Current implementation uses AppleScript to send notifications.
	"""

	IDENTIFIER = "pynotifier.backends.platform.darwin"

	def notify(self, notification: Notification):
		"""
		Send macOS native notification using AppleScript.

		'title' - a title of notification.
		'message' - more info about the notification.
		'sound' - notification sound
		"""
		script = f'display notification "{notification.message}" with title "{notification.title}"'
		sound = notification.config.get('sound', None)
		if sound is not None:
			script += f' sound name "{str(sound)}"'

		command = ['osascript', '-e', script]
		subprocess.Popen(command, shell=False)


Backend = DarwinBackend

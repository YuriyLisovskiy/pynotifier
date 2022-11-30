# Copyright (c) 2022 Yuriy Lisovskiy
#
# Distributed under the MIT licence, see the accompanying file LICENSE.

import subprocess
import platform
from os import walk

from .backend import NotificationBackend
from ..notification import Notification

target_system = platform.system().lower()
if target_system != 'darwin':
	raise SystemError(f'darwin notification backend is not supported on {target_system}')

del target_system


def _load_sounds(p: str):
	try:
		return set(next(walk(p), (None, None, []))[2])
	except FileNotFoundError as exc:
		print(exc)
		return set()


sounds = _load_sounds('/System/Library/Sounds').union(_load_sounds('~/Library/Sounds'))


class DarwinBackend(NotificationBackend):

	IDENTIFIER = "pynotifier.backends.darwin"

	def notify(self, notification: Notification):
		"""
		Sends macOS native notification using AppleScript.

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

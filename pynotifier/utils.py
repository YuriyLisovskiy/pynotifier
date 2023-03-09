"""
This file is a part of py-notifier project.

Copyright (c) 2022-2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from os import environ
from sys import platform as _sys_platform


def get_platform():
	"""
	Determine the current platform using sys.platform.
	"""
	if 'ANDROID_ARGUMENT' in environ:
		return 'android'
	elif _sys_platform in ('win32', 'cygwin', 'windows'):
		return 'windows'
	elif _sys_platform == 'darwin':
		return 'darwin'
	elif _sys_platform.startswith('linux') or _sys_platform.startswith('freebsd'):
		return 'linux'

	return _sys_platform


def assert_system(target: str):
	"""
	Check if the current platform matches target.

	Raises SystemError if the platform does not match.
	"""
	current_system = get_platform().lower()
	if current_system != target:
		raise SystemError(f'{target} notification backend is not supported on {current_system}')

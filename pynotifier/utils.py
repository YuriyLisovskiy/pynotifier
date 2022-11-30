"""
This file is a part of py-notifier project.

Copyright (c) 2022 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

import platform


def assert_system(target: str):
	"""
	Check if current OS matches target.

	Raises SystemError if OS does not match.
	"""
	current_system = platform.system().lower()
	if current_system != target:
		raise SystemError(f'{target} notification backend is not supported on {current_system}')

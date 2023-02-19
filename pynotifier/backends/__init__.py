"""
This file is a part of py-notifier project.

Copyright (c) 2022-2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from pynotifier.backends.backend import NotificationBackend
from pynotifier.backends.smtp import Backend as SMTPBackend

__all__ = ['NotificationBackend', 'SMTPBackend']

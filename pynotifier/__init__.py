"""
Send notifications using backends.
Supported backends can be found in 'pynotifier.backends' module.

This file is a part of py-notifier project.

Copyright (c) 2018, 2021-2022 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from .client import NotificationClient
from .notification import Notification

__all__ = ["NotificationClient", "Notification"]

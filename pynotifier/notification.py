"""
py-notifier: Display desktop notifications using backends for Windows Toast,
             Linux notification etc. More backends can be found in 'pynotifier.backends' module.

Copyright (c) 2018, 2021-2022 Yuriy Lisovskiy

Distributed under the MIT licence,
see the accompanying file LICENSE.
"""


from .backends import notify_all


class Notification:
    """
    Display desktop notifications using registered backends.

    Notification class is just a notification config.
    Call send method to notify all backends.
    """

    def __init__(self, *args, **kwargs):
        """
        Construct with notification properties.

        'title' - a title of notification.
        'message' - more info about the notification.

        Other args are backend-specific.
        """
        self._config = kwargs
        if 'title' not in self._config:
            raise RuntimeError('notification title is required')

    def send(self):
        """Send the notification to all backends."""
        notify_all(
            title=self._config.get('title'),
            message=self._config.get('message', ''),
            **self._config
        )

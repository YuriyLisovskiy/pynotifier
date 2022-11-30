# Copyright (c) 2018, 2021-2022 Yuriy Lisovskiy
#
# Distributed under the MIT licence, see the accompanying file LICENSE.

class Notification:
    """
    Holds notification properties.
    """

    def __init__(self, *args, **kwargs):
        """
        Construct with notification properties.

        Common arguments:
        'title' - a title of notification.
        'message' - more info about the notification.

        Other args are backend-specific.
        """
        self._config = kwargs
        if 'title' not in self._config or self._config.get('title', None) is None:
            raise RuntimeError('notification title is required')

    @property
    def config(self):
        return self._config

    @property
    def title(self):
        return self._config.get('title')

    @property
    def message(self):
        return self._config.get('message', '')
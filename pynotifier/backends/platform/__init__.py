"""
This file is a part of py-notifier project.

Copyright (c) 2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from importlib import import_module

from pynotifier.utils import get_platform

module = import_module('pynotifier.backends.platform.{}'.format(get_platform().lower()))

Backend = module.Backend

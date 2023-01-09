"""
This file is a part of py-notifier project.

Copyright (c) 2022-2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

import platform
from importlib import import_module

module = import_module('pynotifier.backends.{}'.format(platform.system().lower()))

Backend = module.Backend

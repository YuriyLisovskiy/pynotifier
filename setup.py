#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Send notifications using backends.

Copyright (c) 2018, 2021-2022 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

import io
import os

from setuptools import find_packages, setup

NAME = "py-notifier"
DESCRIPTION = "Python push-notifications."
URL = "https://github.com/YuriyLisovskiy/pynotifier"
EMAIL = "yuralisovskiy98@gmail.com"
AUTHOR = "Yuriy Lisovskiy"
REQUIRES_PYTHON = ">=3.6.0"

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "VERSION")) as ver:
    VERSION = tuple([int(x) for x in ver.read(-1).split(".")])

with open(os.path.join(here, "requirements.txt")) as txt:
    REQUIRED = [module_name.rstrip("\n") for module_name in txt.readlines()]

try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=".".join(map(str, VERSION)),
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Full list: https://pypi.org/classifiers
        "Intended Audience :: Information Technology",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Environment :: MacOS X",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Typing :: Typed",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

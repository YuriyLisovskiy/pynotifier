## Desktop Notifications

[![pypi version](https://img.shields.io/pypi/v/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![# of downloads](https://img.shields.io/pypi/dm/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/py-notifier.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/py-notifier)
[![License](https://img.shields.io/github/license/YuriyLisovskiy/pynotifier.svg)](LICENSE)
[![Github Actions](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/tests.yml/badge.svg)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/tests.yml)

Simple Python3 module for displaying desktop notifications on Windows, Linux and MacOS.

### Installation
```bash
$ pip install py-notifier
```

### Requirements
#### Windows:
[`WinToaster`](https://https://github.com/MaliciousFiles/WinToaster) - Python module
#### Linux:
`libnotify-bin` CLI tool (manual installation is required). For Ubuntu run:
```bash
sudo apt-get install libnotify-bin
```
#### MacOS:
[`pync`](https://github.com/SeTeM/pync) - Python module

### Example
```python
from pynotifier import Notification

Notification(
	title='Notification Title',
	description='Notification Description',
	icon_path='/absolute/path/to/image/icon.png', # On Windows .ico is required, on Linux - .png
	duration=5,                                   # Duration in seconds
	urgency='normal'
).send()
```

### Development

[![Tests](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/tests.yml/badge.svg)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/tests.yml)

```bash
$ make
ci               Lint and Test
clean            Remove Python file artifacts and virtualenv
lint             Lint source
test             Run tests
venv             Creates the virtualenv and installs tox
```

### Author
* [Yuriy Lisovskiy](https://github.com/YuriyLisovskiy)

### License
The project is licensed under the terms of the [MIT License](https://opensource.org/licenses/mit),
see the [LICENSE](LICENSE) file for more information.

## Desktop Notifications

[![Github Actions - CI](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/ci.yml/badge.svg)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/ci.yml)
[![Github Actions - Deploy](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/deploy.yml/badge.svg)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/deploy.yml)
[![PyPi Version](https://img.shields.io/pypi/v/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![# of Downloads](https://img.shields.io/pypi/dm/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/py-notifier.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/py-notifier)
[![License](https://img.shields.io/github/license/YuriyLisovskiy/pynotifier.svg)](LICENSE)

Python3 module for sending notifications.

### Installation
```bash
$ pip install py-notifier
```

### Requirements
#### Windows:
[`WinToaster`](https://github.com/MaliciousFiles/WinToaster) - Python module
#### Linux:
`libnotify-bin` CLI tool (manual installation is required). For Ubuntu run:
```bash
sudo apt-get install libnotify-bin
```

### Example
```python
from pynotifier import NotificationClient, Notification
from pynotifier.backends import DesktopBackend

c = NotificationClient()

backend = DesktopBackend()
c.register_backend(backend)

notification = Notification(title='Hello', message='World')
c.notify_all(notification)
```

### License
The project is licensed under the terms of the [MIT License](https://opensource.org/licenses/mit),
see the [LICENSE](LICENSE) file for more information.

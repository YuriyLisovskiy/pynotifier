## Python Notifications

[![Github Actions - CI](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/ci.yml/badge.svg)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/ci.yml)
[![Github Actions - Deploy](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/deploy.yml/badge.svg)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/deploy.yml)
[![PyPi Version](https://img.shields.io/pypi/v/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![# of Downloads](https://img.shields.io/pypi/dm/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/py-notifier.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/py-notifier)
[![License](https://img.shields.io/github/license/YuriyLisovskiy/pynotifier.svg)](LICENSE)

Python3 module for sending notifications.

The list of available backends:
* Platform (`pynotifier.backends.platform.Backend`):
  * macOS
  * Linux
  * Windows
* Email (`pynotifier.backends.smtp.Backend`)

### Platform notifications requirements
#### Windows:
[`WinToaster`](https://github.com/MaliciousFiles/WinToaster) - Python module
#### Linux:
`libnotify-bin` CLI tool (manual installation is required). For Ubuntu run:
```bash
sudo apt-get install libnotify-bin
```

### Installation
```bash
pip install py-notifier
```

### Example
```python
from pynotifier import NotificationClient, Notification
from pynotifier.backends import platform, smtp

c = NotificationClient()

c.register_backend(platform.Backend())
c.register_backend(smtp.Backend(server=smtp.DSMTP_SSL('smtp.gmail.com'),
                                email='sender@email.com',
                                password='super_password'))

notification = Notification(title='Hello',
                            message='World',
                            emails=['receiver_1@email.com', 'receiver_2@email.com'])
c.notify_all(notification)
```

### License
The project is licensed under the terms of the [MIT License](https://opensource.org/licenses/mit),
see the [LICENSE](LICENSE) file for more information.

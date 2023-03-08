# Python Notifications

[![CI](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/ci.yml/badge.svg)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/ci.yml)
[![Deploy](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/deploy.yml/badge.svg?branch=master)](https://github.com/YuriyLisovskiy/pynotifier/actions/workflows/deploy.yml)
[![PyPi Version](https://img.shields.io/pypi/v/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![# of Downloads](https://img.shields.io/pypi/dm/py-notifier.svg)](https://pypi.python.org/pypi/py-notifier)
[![Supported Python Versions](https://img.shields.io/pypi/pyversions/py-notifier.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/py-notifier)
[![License](https://img.shields.io/github/license/YuriyLisovskiy/pynotifier.svg)](LICENSE)

Python3 module for sending notifications.

The list of available backends:
* Platform (`pynotifier.backends.platform.Backend`):
  * Android (Termux)
  * Linux
  * macOS
  * Windows
* Email (`pynotifier.backends.smtp.Backend`)

## Platform notifications requirements
### Android:
[`termux-api`](https://f-droid.org/en/packages/com.termux.api/) - Android application for Termux
### Linux:
`libnotify-bin` CLI tool (manual installation is required). For Ubuntu run:
```bash
sudo apt-get install libnotify-bin
```
### Windows:
[`WinToaster`](https://github.com/MaliciousFiles/WinToaster) - Python module

## Installation
Install using pip:
```bash
pip install py-notifier
```

## Example
```python
import ssl
import smtplib

from pynotifier import NotificationClient, Notification
from pynotifier.backends import platform, smtp

smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl.create_default_context())

c = NotificationClient()

c.register_backend(platform.Backend())
c.register_backend(smtp.Backend(server=smtp_server,
                                name='My Organization',
                                email='sender@organization.com',
                                password='super_password'))

filenames = [
  'path/to/file1.json',
  'path/to/file2.txt',
  # ...
]

attachments = []
for filename in filenames:
	attachments.append(smtp.Attachment(open(filename, 'rb'), filename))

smtp_config = smtp.NotificationConfig(emails=['receiver_1@email.com', 'receiver_2@email.com'],
                                      attachments=attachments)
notification = Notification(title='Hello', message='World', smtp=smtp_config)

c.notify_all(notification)
```

## License
The project is licensed under the terms of the [MIT License](https://opensource.org/licenses/mit),
see the [LICENSE](LICENSE) file for more information.

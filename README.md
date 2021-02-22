## Desktop Notifications

Simple cross-platform (Windows/Linux) Python3 module for displaying desktop notifications.

### Installation
```bash
$ pip install py-notifier
```

### Requirements
#### Windows:
[`win10toast`](https://github.com/jithurjacob/Windows-10-Toast-Notifications) - Python library (will be installed automatically)
#### Linux:
`libnotify-bin` CLI tool (manual installation is required). For Ubuntu run:
```bash
sudo apt-get install libnotify-bin
```

### Example
```python
from pynotifier import Notification


Notification(
	title='Notification Title',
	description='Notification Description',
	icon_path='path/to/image/file/icon.png', # On Windows .ico is required, on Linux - .png
	duration=5,                              # Duration in seconds
	urgency=Notification.URGENCY_CRITICAL
).send()
```

### Author
* [Yuriy Lisovskiy](https://github.com/YuriyLisovskiy)

### License
The project is licensed under the terms of the [GNU General Public License v3.0](https://opensource.org/licenses/GPL-3.0), see the [LICENSE](LICENSE) file for more information.

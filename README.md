## Desktop Notifications

Simple Python3 module for displaying desktop notifications on Windows, Linux and MacOS.

### Installation
```bash
$ pip install py-notifier
```

### Requirements
#### Windows:
[`win10toast`](https://github.com/jithurjacob/Windows-10-Toast-Notifications) - Python module
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
	icon_path='path/to/image/file/icon.png', # On Windows .ico is required, on Linux - .png
	duration=5,                              # Duration in seconds
	urgency='normal'
).send()
```

### Author
* [Yuriy Lisovskiy](https://github.com/YuriyLisovskiy)

### License
The project is licensed under the terms of the [MIT License](https://opensource.org/licenses/mit),
see the [LICENSE](LICENSE) file for more information.

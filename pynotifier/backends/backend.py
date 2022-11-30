import platform


class NotificationBackend:

	def __init__(self, name: str):
		self._name = name

	def notify(self, title: str, message: str, *args, **kwargs):
		raise NotImplemented

	@property
	def name(self):
		return self._name


_backends = dict()


def register_backend(name: str, nb: NotificationBackend):
	if name not in _backends:
		_backends[name] = nb


def notify_all(title: str, message: str, *args, **kwargs):
	for backend in _backends:
		_backends[backend].notify(title=title, message=message, *args, **kwargs)


_target_system = platform.system().lower()

_darwin = 'darwin'


def register_system_backend():
	notification_backend = None
	if _target_system == _darwin:
		from .darwin import DarwinNB
		notification_backend = DarwinNB()
	else:
		raise SystemError(
			"notifications are not supported for {} system".format(_target_system)
		)

	register_backend('system', notification_backend)

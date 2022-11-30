import subprocess

from .backend import NotificationBackend, _target_system, _darwin

if _target_system != _darwin:
	raise SystemError(f'{_darwin} notification backend is not supported on {_target_system}')

# try:
# 	import pync
# except ImportError:
# 	raise ImportError("notifications are not supported, can't import pync")


HeroSound = 'Hero'
GlassSound = 'Glass'


class DarwinNB(NotificationBackend):

	def __init__(self):
		super().__init__('darwin')

	def notify(self, title: str, description: str, *args, **kwargs):
		script = f'display notification "{description}" with title "{title}"'
		sound = kwargs.get('sound', None)
		if sound is not None:
			script += f' sound name "{str(sound)}"'

		command = ['osascript', '-e', script]
		subprocess.Popen(command, shell=False)
	# 	pync.notify(message=description, title=title, appIcon=kwargs.get('icon_path', None))

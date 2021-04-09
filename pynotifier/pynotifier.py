# py-notifier
# Copyright (c) 2018, 2021 Yuriy Lisovskiy
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__all__ = ['Notification']

# standard library
import platform


# class to run notification
class Notification:

	# 'title' - a title of notification.
	# 'description' - more info about the notification.
	# 'duration' - notification timeout in seconds.
	# 'urgency' - notification urgency level (ignored under Windows);
	#             possible values: 'low', 'normal', 'critical'.
	# 'icon_path' - path to notification icon file.
	def __init__(self, title, description='', duration=5, urgency='low', icon_path=None):
		if title is None:
			raise ValueError('title with None value is not allowed')

		if title == '':
			raise ValueError('title must not be empty')

		system = platform.system().lower()
		if 'windows' in system:
			self.__sender = self.__send_windows
		elif 'linux' in system:
			if urgency not in ['low', 'normal', 'critical', None]:
				raise ValueError('invalid urgency was given: {}'.format(urgency))

			self.__sender = self.__send_linux
		else:
			raise SystemError('notifications are not supported for {} system'.format(system))

		self.__title = title
		self.__description = description
		self.__duration = duration
		self.__urgency = urgency
		self.__icon_path = icon_path

	# sends notification using '__sender'
	def send(self):
		self.__sender()

	# sends notification if running on Linux system
	def __send_linux(self):
		import subprocess
		command = [
			'notify-send', '{}'.format(self.__title),
			'{}'.format(self.__description),
			'-t', '{}'.format(self.__duration * 1000)
		]
		if self.__urgency is not None:
			command += ['-u', self.__urgency]

		if self.__icon_path is not None:
			command += ['-i', self.__icon_path]

		subprocess.call(command)

	# sends notification if running on Windows system
	def __send_windows(self):
		try:
			import win10toast
			win10toast.ToastNotifier().show_toast(
				threaded=True,
				title=self.__title,
				msg=self.__description,
				duration=self.__duration,
				icon_path=self.__icon_path
			)
		except ImportError:
			raise ImportError('notifications are not supported, can\'t import necessary library')

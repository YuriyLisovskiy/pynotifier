"""
This file is a part of py-notifier project.

Copyright (c) 2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from os.path import split as split_path
import smtplib
from typing import BinaryIO

from pynotifier.notification import Notification

from .backend import NotificationBackend


class Attachment:
	"""Attachment is a lazy reader for BinaryIO object.
	It holds a tail of filename and loads binary data
	from reader when it requested for the first time.

	"""

	def __init__(self, reader: BinaryIO, filename: str):
		self._reader = reader
		self._data = None

		# Get tail of filename, i.e. if the filename is "/path/to/file.txt"
		# we retrieve "file.txt" here.
		self._filename = split_path(filename)[1]

	@property
	def data(self):
		if self._data is None:
			self._data = self._reader.read()

		return self._data

	@property
	def filename(self):
		return self._filename


class NotificationConfig:
	"""NotificationConfig holds a list of receivers emails and attachments.

	"""
	def __init__(self, emails: [str], attachments: [Attachment]):
		self.emails = emails
		self.attachments = attachments


class Backend(NotificationBackend):
	"""SMTP notification backend.
	name: str - the name for email 'From' field
	mime_type: [str], default: "plain"

	Additional parameters for Notification.Config object:
	 - smtp: NotificationConfig

	Note: info about how to send email from Google Mail with App Password:
	https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84

	"""
	IDENTIFIER = 'pynotifier.backends.smtp'

	def __init__(self,
	             server: smtplib.SMTP,
	             email: str,
	             password: str,
	             name: str = '',
	             mime_type: str = 'plain',
	             *args,
	             **kwargs):
		"""Initialize the SMTPBackend.
		If the SMTP server supports authentication, the backend will log in automatically.

		"""
		super().__init__(*args, **kwargs)
		self._server = server
		self._name = name
		self._email = email
		if self._name == '':
			self._name = self._email

		self._password = password
		self._mime_type = mime_type

		try:
			self._server.login(self._email, self._password)
		except smtplib.SMTPNotSupportedError:
			pass

	def notify(self, notification: Notification):
		"""Send the notification using config from Notification object.

		"""
		config = notification.config.get('smtp', '')
		if not isinstance(config, NotificationConfig):
			raise TypeError('invalid notification config for SMTP Backend')

		for to_email in config.emails:
			message = self._get_multipart_message(notification.title,
			                                      notification.message,
			                                      to_email,
			                                      config)
			self._server.sendmail(self._email, to_email, message.as_string())

	def _get_multipart_message(self, title: str, message: str, to_email: str, config: NotificationConfig):
		m = MIMEMultipart()
		m['Subject'] = title
		m['From'] = self._name
		m['To'] = to_email

		m.attach(MIMEText(message, self._mime_type))

		for attachment in config.attachments:
			part = self._get_attachment_part(attachment)
			m.attach(part)

		return m

	@staticmethod
	def _get_attachment_part(attachment):
		part = MIMEBase('application', 'octet-stream')
		part.set_payload(attachment.data)

		encoders.encode_base64(part)

		part.add_header('Content-Disposition',
		                f'attachment; filename= {attachment.filename}')

		return part

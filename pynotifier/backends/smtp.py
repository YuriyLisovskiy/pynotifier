"""
This file is a part of py-notifier project.

Copyright (c) 2023 Yuriy Lisovskiy

Distributed under the MIT licence, see the accompanying file LICENSE.
"""

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pynotifier.notification import Notification
from .backend import NotificationBackend


class DSMTP_SSL(smtplib.SMTP_SSL):
	"""DSMTP_SSL - SMTP protocol with default SSL context and port.

	"""
	SSL_PORT = 465

	def __init__(self, host, *args, **kwargs):
		super().__init__(host, self.SSL_PORT, context=ssl.create_default_context(), *args, **kwargs)


# TODO: add attachments to email from notification.config!
class Backend(NotificationBackend):
	"""SMTP notification backend.
	mime_type: [str], default: "plain"

	Additional parameters for Notification.Config object:
	 - emails: [str]

	Note: info about how to send email from Google Mail with App Password:
	https://levelup.gitconnected.com/an-alternative-way-to-send-emails-in-python-5630a7efbe84

	"""
	IDENTIFIER = 'pynotifier.backends.smtp'

	def __init__(self,
	             server: smtplib.SMTP,
	             email: str,
	             password: str,
	             mime_type: str = 'plain',
	             *args,
	             **kwargs):
		"""Initialize the SMTPBackend.
		If the SMTP server supports authentication, the backend will log in automatically.

		"""
		super().__init__(*args, **kwargs)
		self._server = server
		self._email = email
		self._password = password
		self._mime_type = mime_type

		try:
			self._server.login(self._email, self._password)
		except smtplib.SMTPNotSupportedError:
			pass

	def notify(self, notification: Notification):
		"""Send the notification using config from Notification object.

		"""
		to_emails = notification.config.get('emails', '')
		for to_email in to_emails:
			self._send_notification(to_email, notification)

	def _send_notification(self, to_email: str, notification: Notification):
		message = self._get_message(notification, to_email)
		self._server.sendmail(self._email, to_email, message.as_string())

	def _get_message(self, notification: Notification, to_email: str):
		message = MIMEMultipart()
		message['Subject'] = notification.title
		message['From'] = self._email
		message['To'] = to_email

		message.attach(MIMEText(notification.message, self._mime_type))

		return message

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


class SMTPBackend(NotificationBackend):
	"""SMTP notification backend.

	"""
	IDENTIFIER = 'pynotifier.backends.smtp'

	def __init__(self, email, password, *args, **kwargs):
		"""TODO:

		"""
		super().__init__(*args, **kwargs)
		self._ssl_port = 465
		self._email = email
		self._password = password
		self._ssl_context = ssl.create_default_context()
		self._server = smtplib.SMTP_SSL("smtp.gmail.com", self._ssl_port, context=self._ssl_context)
		self._server.login(self._email, self._password)

	def notify(self, notification: Notification):
		"""Send the notification using config from Notification object.

		"""
		receiver_email = notification.config.get('email', '')
		message = self._get_message(notification, receiver_email)
		self._server.sendmail(self._email, receiver_email, message.as_string())

	def _get_message(self, notification: Notification, receiver_email: str):
		"""Builds MIMEMultipart message from notification options.
		Note: receiver_email is received from notification.config.

		"""
		message = MIMEMultipart()
		message["From"] = self._email
		message["To"] = receiver_email
		message["Subject"] = notification.title

		# Recommended for mass emails
		message["Bcc"] = receiver_email

		message.attach(MIMEText(notification.message, notification.config.get('mime_type', 'plain')))

		return message

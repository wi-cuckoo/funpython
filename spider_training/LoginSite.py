#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import sys

class loginsite:
	
	def __init__(self, login_url, headers={}, **user_info):
		self.login_url = login_url
		self.headers = headers
		self.user_info = user_info
		
		try:
			self.session = requests.Session()
		except:
			print "Sorry, can't create a session, exit"
			sys.exit()

	def login(self):
		try:
			response = self.session.post(self.login_url, data=self.user_info, 
					headers=self.headers, allow_redirects=False
					)
			if response.ok:
				self.handle_response(response)
		except requests.exceptions.RequestException, e:
			print str(e)
			sys.exit()
		return True

	def handle_response(self, res):
		self.cookies = res.cookies
		if res.status_code == 302:
			location_url = res.headers['Location']
			self.session.get(location_url, cookies=self.cookies)

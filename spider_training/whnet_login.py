#! /usr/bin/env python
# -*- coding:utf-8 -*-

from HTMLParser import HTMLParser, HTMLParseError
import requests
import re
import sys

class Whnet:

	def __init__(self, **user):
		self.username = user.get('username', 'guest')
		self.password = user.get('password', 'guest')
		self.login_url = 'http://bbs.whnet.edu.cn/cgi-bin/bbslogin'

	def login(self):
		user_info = {'id':self.username, 'pw':self.password}
		try:
			res = requests.post(self.login_url, data=user_info)
		except requests.exceptions.RequestException, e:
			print str(e)
			sys.exit()
		else:
			print res.status_code, '\t', res.reason
			self.__parse_cookies(res.text)
	
	def __parse_cookies(self, body):
		self.cookies = {}
		pattern = re.compile(r'utmp[a-z0-9=]+')
		cookies_match = pattern.findall(body)
		for item in cookies_match[3:]:
			temp_list = item.split('=')
			self.cookies[temp_list[0]] = temp_list[1]
	
	def logout(self):
		logout_url = 'http://bbs.whnet.edu.cn/cgi-bin/bbslogout'
		r = requests.get(logout_url)
		if r.ok:
			print 'Logout Succ'

class MailList_HTMLParser(HTMLParser):
	
	def handle_starttag(self, tag, attrs):
		pass
	
	def handle_data(self, data):
		print data.strip()	
			

class Whnet_UserInfo(Whnet):
	
	def get_commend_list(self):
		'''Get the first 5 list whose name begin without 【'''
		pass

	def get_bbs_mail(self):
		''' Get the latest 10 mails from inbox'''
		mail_url = 'http://bbs.whnet.edu.cn/cgi-bin/bbsmail'
		r = requests.get(mail_url, cookies=self.cookies)
		if r.ok:
			try:
				list_parser = MailList_HTMLParser()
				list_parser.feed(r.text)
			except HTMLParseError:
				print 'html parser error'
			finally:
				list_parser.close()
		

def main():
	headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate, sdch',
		'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ru;q=0.2',
		'Connection': 'keep-alive',
		'Host': 'bbs.whnet.edu.cn',
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36'
		}
	user = {'username':'sb', 'password':'sb'}

	my_whnet = Whnet_UserInfo(**user)
	my_whnet.login()
	my_whnet.get_bbs_mail()
	my_whnet.logout()

if __name__ == '__main__':
	main()



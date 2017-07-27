#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re
from LoginSite import loginsite

class hudbtlogin(loginsite):
	
	def logout(self):
		self.session.close()
		sys.exit()
	
	def get_torrent_page(self):
		torrent_url = 'https://hudbt.hust.edu.cn/torrents.php'
		# this get requests can't send headers, important!
		r = self.session.get(torrent_url, cookies=self.cookies)
		print r.text		

def main():
	user_info = {'username': 'sb', 'password': 'sb'}
	headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'accept-encoding': 'gzip, deflate',
		'accept-language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,ru;q=0.2',
		'content-length': '40',
		'content-type': 'application/x-www-form-urlencoded',
		'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/49.0.2623.108 Chrome/49.0.2623.108 Safari/537.36',
		}	
	login_url = 'https://hudbt.hust.edu.cn/takelogin.php'
	
	hudbt = hudbtlogin(login_url, headers=headers, **user_info)
	hudbt.login()
	hudbt.get_torrent_page()
	hudbt.logouth()

if __name__ == '__main__':
	main()

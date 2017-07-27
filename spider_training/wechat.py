#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import os, sys
import time
import urllib
import json

class Wechat:
	
	def __init__(self):
		try:
			self.session = requests.Session()
		except:
			print "Can't create a session, exit"
			sys.exit()

	def __get_uuid(self):
		url = 'https://login.weixin.qq.com/jslogin'
		json_params = {
			'appid': 'wx782c26e4c19acffb',
			'redirect_uri': 'https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/webwxnewloginpage',
			'fun': 'new',
			'lang': 'en_US',
			'_': int(time.time()),
			}
		r = self.session.post(url, data=urllib.urlencode(json_params), allow_redirects=True)
		res_data = r.content
		if res_data[22:25] == '200':
			self.uuid = r.content[-14:-2]
		else:
			print "Get UUID failed, system exit!"
			sys.exit()

	def __get_qrcode(self):
		qr_url = 'https://login.weixin.qq.com/qrcode/' + self.uuid
		params = {
                	't': 'webwx',
                	'_': int(time.time()),
		        }
		r = self.session.get(qr_url, data=urllib.urlencode(params))
		
		try:
			f = open('./qrcode.jpg', 'wb')
			f.write(r.content)
			f.close()
		except:
			print "Create QR image failed!"
		
		os.system('xdg-open ./qrcode.jpg')
		print 'Please scan the QR code to login'

	def login(self):
		self.__get_uuid()
		self.__get_qrcode()		

		login_url = 'https://login.weixin.qq.com/cgi-bin/mmwebwx-bin/login?tip=%s&uuid=%s&_=%s' % ('0', self.uuid, int(time.time()))
		self.redirect_uri = 'fuck'
		def scan_qrcode():
			response = self.session.get(login_url)
			re_text = response.content
			status_code = re_text[12:15]
			if status_code == '408':
				print "Timeout, Please try again"
			elif status_code == '200':
				print "loading..."
				re_uri = r'window.redirect_uri="(\S+?)";'
				pattern_match = re.search(re_uri, re_text)
				self.redirect_uri = pattern_match.group(1) + '&fun=new'
			return status_code
	
		while scan_qrcode() != '200':
			pass
		#os.system('rm -f ./qrcode.jpg')
		#print self.redirect_uri
		try:
			r = self.session.get(self.redirect_uri)
			if r.ok:
				print "Login Succ, enjoy yourself!"
		except:
			print "Login failed, please try later!"
			
		p = re.compile(r'<skey>(.*?)</skey><wxsid>(.*?)</wxsid><wxuin>(.*?)</wxuin>' +
				r'<pass_ticket>(.*?)</pass_ticket>', re.S)
		m = p.findall(r.content)

		self.pass_ticket = m[0][3]
		self.BaseRequest = {
			'Skey': m[0][0],
			'Sid': m[0][1],
			'Uin': int(m[0][2]),
			'DeviceID': 'e000000000000000',
			}
	
	def logout(self):
		logout_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxlogout?redirect=1&type=0&skey=%s' % self.BaseRequest['Skey']
		#headers = {'Content-Type': 'application/x-www-form-urlencoded'}
		params = {
			'uin': self.BaseRequest['Uin'],
			'sid': self.BaseRequest['Sid'],
			}

		try:
			r = self.session.post(logout_url, data=urllib.urlencode(params), allow_redirects=True)
			if r.ok:
				print 'Logout Succ, Bye!'
		except:
			print 'The fucking error occurred'
		finally:
			self.session.close()
			print "Session has been closed!"
		return True

class enjoyWechat(Wechat):
	
	def __init__(self):
		Wechat.__init__(self) 
		self.base_uri = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/'

	def get_contacts_list(self, filename='./wxcontact.json'):
		wxinit_url = self.base_uri + 'webwxgetcontact?pass_ticket=%s&skey=%s&r=%s' % (self.pass_ticket, self.BaseRequest['Skey'], int(time.time()))
		params = { 'BaseRequest': self.BaseRequest}
		headers = {'ContentType': 'application/json; charset=UTF-8'}
		r = self.session.post(wxinit_url, json=params, headers=headers)
		data = r.content
		if filename:
			f = open(filename, 'wb')
			f.write(data)
			f.close()

		Contact_List = json.loads(data)['MemberList']
		Contact_Dic = {}
		for item in Contact_List:
			if item['NickName'] == 'Wi':
				self.MyUserName = item['UserName']
			Contact_Dic[item['NickName']] = item
			
		return Contact_Dic
	
	def send_text_to_someone(self, text, UserName):
		sendtext_url = self.base_uri + 'webwxsendmsg?lang=en_US&pass_ticket=%s' % self.pass_ticket
		headers = {'ContentType': 'application/json; charset=UTF-8'}
		payload = {
			'BaseRequest': self.BaseRequest,
			'Msg':{
				'ClientMsgId': "14606351616150274",
				'Content': text,
				'FromUserName': self.MyUserName,
				'LocalID': "14606351616150274",
				'ToUserName': UserName,
				'Type': 1,
				}
			}
		
		r = self.session.post(sendtext_url, json=payload, headers=headers)
		print r.content

def main():
	user = enjoyWechat()
	user.login()
	try:
		contact = user.get_contacts_list()
		user.send_text_to_someone('Love you forever', contact['樱花炒饭'.decode('utf-8')]['UserName'])
	except:
		print "Fuck"
	user.logout()

if __name__=='__main__':
	main()

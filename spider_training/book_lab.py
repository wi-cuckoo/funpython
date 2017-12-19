#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import pytesseract
import time
from datetime import date, timedelta
from PIL import Image
from bs4 import BeautifulSoup

# global const variable
HOST = '115.156.150.131'
TIME_ARR = ['08:00', '08:30', '09:00', '09:30',
			'10:00', '10:30', '11:00', '11:30',
			'14:00', '14:30', '15:00', '15:30',
			'16:00', '16:30', '17:00', '17:30']
# set the tesseract cmd path
pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'


class BookLab(object):
	csrftoken = ''
	sessionid = ''

	def __init__(self, user, passwd):
		self.user = user
		self.passwd = passwd
		self.session = requests.Session()

	# deprecated
	@property
	def cookies(self):
		cookies = dict()
		if self.csrftoken != '':
			cookies['csrftoken'] = self.csrftoken
		if self.sessionid != '':
			cookies['sessionid'] = self.sessionid
		return cookies

	def get_csrftoken(self, url):
		r = self.session.get(url)
		if not r.ok:
			print 'get login page error: ', r.reason
			return None
		return r.cookies.get('csrftoken')

	def login(self):
		login_url = 'http://%s/admin/login/?next=/admin/' % HOST
		csrftoken = self.get_csrftoken(login_url)
		if csrftoken is None:
			return

		payload = {
			'csrfmiddlewaretoken': csrftoken,
			'username': self.user,
			'password': self.passwd,
			'next': '/admin/'
		}
		r = self.session.post(
			'http://%s/admin/login/?next=/admin/' % HOST,
			cookies=dict(csrftoken=csrftoken),
			allow_redirects=False,
			data=payload)
		if not r.ok:
			print 'login failed: ', r.reason
			return
		self.sessionid = r.cookies.get('sessionid')
		return True

	def __parse_code(self, captcha):
		verify_img_url = 'http://%s/captcha/image/%s' %(HOST, captcha)
		# store temporary image
		filepath = '/tmp/captcha.png'
		r = self.session.get(verify_img_url)
		with open(filepath, 'wb') as f:
			f.write(r.content)

		return 'xxxx'  # fake return
		# return pytesseract.image_to_string(Image.open(filepath))

	def __parse_captcha(self, markup):
		soup = BeautifulSoup(markup, 'lxml')
		captcha_el = soup.find('input', id='id_captcha_0')
		return captcha_el.get('value')

	def __parse_result(self, markup):
		soup = BeautifulSoup(markup, 'lxml')
		errlist = soup.find('ul', class_='errorlist')
		msg = '\n'.join([el.string for el in errlist.children])
		return msg


	def book_submit(self, _date, _time):
		# notice: get will response a new csrf_token
		add_page_url = 'http://%s/admin/reserve/reserve/add/' % HOST
		r = self.session.get(add_page_url)
		if not r.ok:
			return

		csrftoken = r.cookies.get('csrftoken')
		captcha = self.__parse_captcha(r.content)
		code = self.__parse_code(captcha)
		
		# cacl the lab date
		today = date.today()
		labdate = today + timedelta(days=7)
		if _date is not None:
			labdate = _date

		payload = {
			'csrfmiddlewaretoken': csrftoken,
			'name': '姚琴',
			'teacher': '吴丰顺',
			'teacher_pay': 'A44',
			'device': '13',
			'teleph': '13986272487',
			'descript': 'hello everyone',
			'regdate': today.strftime('%Y/%m/%d'),
			'labdate': labdate.strftime('%Y/%m/%d'),
			'labinfo': '2个Si样品',
			'starttime': _time['start'],
			'endtime': _time['end'],
			'material': 'Al',
			'depth': '60',
			'number': '1',
			'temperature': '0',
			'count_person': '1',
			'count_taoke': '0',
			'count_untaoke': '0',
			'captcha_0': '8213f0ea7757c455da0aab8931e45cad00b7741c',
			'captcha_1': 'EZEW',
			'_save': '保存'
		}
		cookies = dict(csrftoken=csrftoken, sessionid=self.sessionid)
		r = self.session.post(add_page_url, data=payload, cookies=cookies)
		if not r.ok:
			print 'submit the book form data: Failed'
			return

		msg = self.__parse_result(r.content)
		if msg != '':
			return msg
		return True


	def __del__(self):
		r = self.session.get('http://%s/admin/logout/' % HOST)
		print '\nlogout result: ', r.ok


	def run(self, d=None):
		"""
		t should be datetime.date object
		"""
		if self.login() is None:
			print 'Login Failed, Exit'
			return		
		print 'Login successfully, sessionid is ', self.sessionid

		tm = time.strftime('%H:%M')
		if time.strptime(tm, '%H:%M') < time.strptime('07:59', '%H:%M'):
			return
		# submit the book form
		count = 1
		while count < 5000:
			print '\nTry %d times' % count
			for x in xrange(len(TIME_ARR)-3):
				t = {'start': TIME_ARR[x], 'end': TIME_ARR[x+2]}
				print 'book time range is %s - %s :' %(t['start'], t['end']),
				res = self.book_submit(d, t)
				if res == True:
					print 'OK'
					return
				print 'Failed', res

if __name__ == '__main__':
	bl = BookLab('yaoqin', '123456')
	bl.run()
#! /usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import pytesseract
import time
from datetime import date, timedelta
from PIL import Image, ImageOps
from bs4 import BeautifulSoup

# global const variable
HOST = '115.156.150.131'
TIME_ARR = [['08:00', '11:30'], 
			['15:30', '17:00']]

# set the tesseract cmd path
tessdata_dir_config = '--tessdata-dir "/usr/local/share/tessdata"'
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


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
		filepath = '/tmp/captcha/%s.png' % captcha
		r = self.session.get(verify_img_url)
		with open(filepath, 'wb') as f:
			f.write(r.content)

		def init_table(threshold=134):
			table = []
			for i in range(256):
				if i < threshold:
					table.append(0)
				else:
					table.append(1)
			return table
		im = Image.open(filepath) \
			.convert('L') \
			.point(init_table(), '1') \
			.convert('L')
		im = ImageOps.invert(im) \
			.convert('1') \
			.convert('L') \
			.resize((120, 50))

		return pytesseract.image_to_string(im, config=tessdata_dir_config)

	def __parse_captcha(self, markup):
		soup = BeautifulSoup(markup, 'lxml')
		captcha_el = soup.find('input', id='id_captcha_0')
		return captcha_el.get('value')

	def __parse_result(self, markup):
		soup = BeautifulSoup(markup, 'lxml')
		errlist = soup.find_all('ul', class_='errorlist')
		msg = '\n'.join([el.string for err in errlist for el in err.children])
		return msg


	def book_submit(self, _date, _time):
		# notice: get will response a new csrf_token
		add_page_url = 'http://%s/admin/reserve/reserve/add/' % HOST
		r = self.session.get(add_page_url)
		if not r.ok:
			return

		csrftoken = r.cookies.get('csrftoken')
		captcha = self.__parse_captcha(r.content)
		code = self.__parse_code(captcha)[0:4]
		print code
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
			'starttime': _time[0],
			'endtime': _time[1],
			'material': 'Al',
			'depth': '60',
			'number': '1',
			'temperature': '0',
			'count_person': '1',
			'count_taoke': '0',
			'count_untaoke': '0',
			'captcha_0': captcha,
			'captcha_1': code,
			'_save': '保存'
		}
		cookies = dict(csrftoken=csrftoken, sessionid=self.sessionid)
		r = self.session.post(add_page_url, data=payload, cookies=cookies)
		if not r.ok:
			print 'submit the book form data failed: ', r.reason
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

		range_one = ('07:59:00', '08:01:00')
		range_two = ('15:29:00', '15:31:00')
		def in_range(t, r):
			t = time.strptime(t, '%H:%M:%S')
			r0 = time.strptime(r[0], '%H:%M:%S')
			r1 = time.strptime(r[1], '%H:%M:%S')
			return t > r0 and t < r1
		# submit the book form
		count = 1
		while True:
			tr = []
			tm = time.strftime('%H:%M:%S')
			if in_range(tm, range_one):
				tr = TIME_ARR[0]
			if in_range(tm, range_two):
				tr = TIME_ARR[1]

			if len(tr) == 0:
				print 'Waiting.....%s\r' % tm,
				time.sleep(1)
				continue

			print '\nTry %d times' % count
			count += 1
			print 'book time range is %s - %s :' %tuple(tr),
			res = self.book_submit(d, tr)
			if res == True:
				print 'OK'
				return
			print 'Failed \n', res

if __name__ == '__main__':
	bl = BookLab('yaoqin', '123456')
	bl.run()
'''
This little spider is to crawl something funny from qiushibaike.com
Latest Update: 2016/4/27
by Wi
'''
#! /usr/bin/env python
# -*- coding=utf-8 -*-

import requests
import sys
import re
import term

reload(sys)
sys.setdefaultencoding('utf-8')

# Create a class to handle some methods
class Qiushibaike:
	
	def __init__(self, url, **headers):
		self.url = url
		self.headers = headers
		try:
			self.session = requests.Session()
		except:
			print "Sorry, can't initialize a session"
			sys.exit()

	def get_main_page(self):
		try:	
			r = self.session.get(self.url)
			return r.text
		except:
			print "Can't get the main page"
			sys.exit()	
		
	def parse_page(self, content):
		"""get all issues in main page(default page 1)
		every issue will include author, content, like, and comment count
		"""
		article_block = re.findall(r'<div.*?article\sblock.*?>(.*?)<div\sid', content, re.S)
		
		def div_block(block):
			pattern = re.compile(r'<div.*?uthor clearfix">(.*?)</div>.*?' +
				r'<div.*?content">(.*?)</div>.*?' + 
				r'<div.*?stats">(.*?)</div>', re.S)
			div_chunk = pattern.findall(block)
			return div_chunk[0]
		def haveImg(block):
			m = re.search(r'<div class="thumb">', block)
			return m
		def output(item):
			author = re.search(r'<h2>(.*?)</h2>', item[0], re.S)
			#text = re.search(r'(.*)', item[1], re.S)
			text = item[1]
			other_info = re.findall(r'<i.+?number">(\d+)</i>\s(\S+?)\s?<', item[2], re.S)
			
			term.writeLine(author.group(1), term.green, term.blink)
			term.writeLine(text.replace('<br/>', '\n').strip(), term.yellow)
			# do like this in case of no fun or comment
			for info in other_info:
				term.write(info[0]+info[1]+'\t', term.blue)
			else:
				print '\n'

		for block in article_block:
			if haveImg(block):
				continue
			item = div_block(block)
			try:
				output(item)
			except:
				pass		

	def start(self):
		res_content = self.get_main_page()
		self.parse_page(res_content)

def main():
	url = 'http://www.qiushibaike.com'
	robot = Qiushibaike(url)
	robot.start()

if __name__ == '__main__':
	main()

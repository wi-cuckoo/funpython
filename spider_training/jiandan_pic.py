#! /usr/bin/env python
# _*_ coding=utf-8 _*_

import requests
import re
import sys, os
from threading import Thread

class Jiandan_ooxx:

	def __init__(self, path='./beautyImg/'):
		self.main_url = 'http://jandan.net/ooxx/'
		self.session = requests.Session()
		self.path = path
		
		try:
			os.makedirs(self.dir_path)
		except:
			pass

	def get_htmlpage(self, page):
		page_url = self.main_url + 'page-' + str(page)
		self.new_path = self.path + str(page) + '/'
		os.makedirs(self.new_path)
		try:
			r = self.session.get(page_url)
			return r.text
		except requests.exceptions.RequestException, e:
			print str(e)
			sys.exit()
	
	def parse_imageUrl(self, text):
		commentlist = re.search(r'<ol.*?commentlist.*?>(.*?)</ol>', text, re.S)
		li_block = re.findall(r'<li id="comment.*?>(.*?)</li>', commentlist.group(1), re.S)
		
		for item in li_block:
			img_url = re.search(r'<img\s*src="(.*?)".*?/>', item, re.S)
			if img_url == None:
				return
			self.storeImage(img_url.group(1))

	def storeImage(self, img_url):
		try:
			r = self.session.get(img_url)
		except:
			print "Can't get this pic from", img_url
			return
		filename = self.new_path + img_url.split('/')[-1]
		try:
			f = open(filename, 'wb')
			f.write(r.content)
			print 'Saved to %s from %s' %(filename, img_url)
		except IOError, e:
			print str(e)
		finally:
			f.close()

	def begin(self, page):
		page_content = self.get_htmlpage(page)
		self.parse_imageUrl(page_content)
	
def main():
	threadpool = []
	for page in xrange(1500, 1665):
		mm_spider = Jiandan_ooxx()
		t = Thread(target=mm_spider.begin, args=(page,))
		threadpool.append(t)
	
	for thread in threadpool:
		thread.start()		

	for thread in threadpool:
		thread.join()

if __name__ == '__main__':
	main()

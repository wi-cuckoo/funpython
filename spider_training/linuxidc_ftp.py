#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup

ROOT_URL = 'http://linux.linuxidc.com/'


class LinuxIDCCrawl:

	def __init__(self):
		self.session = requests.Session()

	def run(self):
		r = self.session.get(ROOT_URL)
		if not r.ok:
			return

		soup = BeautifulSoup(r.content, "html.parser")
		print soup.find_all('a', href=re.compile('folder='))


if __name__ == '__main__':
    LinuxIDCCrawl().run()

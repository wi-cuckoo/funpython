#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
author: wi
date: 2016/6/29
comment: everything is ok!
'''

__version__ = 'v0.0.1'

from pymongo import MongoClient

class MongoQuery:
	def __init__(self):
		self.client = MongoClient()
	
	def _get_db(self):
		db_list = []
		for db in self.client.database_names():
			db_list.append(self.client[db])
		return db_list
	
	def _get_col(self, db):
		col_list = []
		for col in db.collection_names():
			col_list.append(db[col]) 
		return col_list

	def _get_doc(self, col):
		doc_list = []
		for doc in col.find():
			doc_list.append(doc)	
		return doc_list
	
	def query_all(self):
		for db_object in self._get_db():
			print db_object.name
			for col_ob in self._get_col(db_object):
				print '\n' + '+'*6 + col_ob.name
				for doc in self._get_doc(col_ob):
					print '\n' + '+'*12 + str(doc)

if __name__ == '__main__':
	query = MongoQuery()
	query.query_all()	

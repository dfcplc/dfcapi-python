# -*- coding:utf-8 -*-

import sys
import os
import unittest


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import dfcapi

amounts = [10,10,10,10,10,10,10,10,10,10,10,10]

class DfcapiTestCase(unittest.TestCase):

#  CHECKKEY
	def test_checkkey(self):
		dfcapi.setCheckKeyUrl('http://httpbin.org/get')
		response = dfcapi.checkApiKey('TEST-TEST-TEST-TEST','fee78bd3bf59bfb36238b3f67de0a6ea103de130')
		self.assertEqual(response.code, 200)
		self.assertEqual(response.body['headers']['Authorization'], "Basic VEVTVC1URVNULVRFU1QtVEVTVDpmZWU3OGJkM2JmNTliZmIzNjIzOGIzZjY3ZGUwYTZlYTEwM2RlMTMw")

#  View Direct debits
	def test_ViewDirectDebits(self):
		dfcapi.setViewDirectDebitUrl('http://httpbin.org/get')
		response = dfcapi.ViewDirectDebits('TEST-TEST-TEST-TEST','fee78bd3bf59bfb36238b3f67de0a6ea103de130','000101AA0001')		
		self.assertEqual(response.code, 200)
		self.assertEqual(response.body['headers']['Authorization'], "Basic VEVTVC1URVNULVRFU1QtVEVTVDpmZWU3OGJkM2JmNTliZmIzNjIzOGIzZjY3ZGUwYTZlYTEwM2RlMTMw")
 		self.assertEqual(response.body['args']['dfc_reference'], "000101AA0001")

#  View Direct debits Breakdown
	def test_ViewDirectDebitsBreakdown(self):
		dfcapi.setViewDirectDebitBreakdownUrl('http://httpbin.org/get')
		response = dfcapi.ViewDirectDebitsBreakdown('TEST-TEST-TEST-TEST','fee78bd3bf59bfb36238b3f67de0a6ea103de130','000101AA0001')		
		self.assertEqual(response.code, 200)
		self.assertEqual(response.body['headers']['Authorization'], "Basic VEVTVC1URVNULVRFU1QtVEVTVDpmZWU3OGJkM2JmNTliZmIzNjIzOGIzZjY3ZGUwYTZlYTEwM2RlMTMw")
 		self.assertEqual(response.body['args']['dfc_reference'], "000101AA0001")
		
#  Create Direct Debits
	def test_createDirectDebit(self):
		dfcapi.setCreateDirectDebitUrl('http://httpbin.org/post')
		response = dfcapi.createDirectDebit('TEST-TEST-TEST-TEST','fee78bd3bf59bfb36238b3f67de0a6ea103de130','0001','ABC00001','Mr','Joe','Bloggs','1 Park Lane','','','London','','E15 2JG',amounts,'joebloggs@email.com','00000000','000000','2015-01-01',12,1,'MONTH','Y','1970-01-01','01234567890','07777777777','Y','Gym Membership','',False)				
		self.assertEqual(response.code, 200)
		self.assertEqual(response.body['data'], '{"payer": {"birth_date": "1970-01-01", "first_name": "Joe", "last_name": "Bloggs", "title": "Mr"}, "authentication": {"apikey": "TEST-TEST-TEST-TEST", "apisecret": "fee78bd3bf59bfb36238b3f67de0a6ea103de130", "club_ref_no": "0001"}, "contact": {"phone_number": "07777777777", "no_email": "Y", "email": "joebloggs@email.com", "mobile_number": "01234567890"}, "address": {"town": "London", "address1": "1 Park Lane", "address2": "", "address3": "", "county": "", "postcode": "E15 2JG", "skip_check": false}, "bank": {"sort_code": "000000", "account_number": "00000000"}, "subscription": {"reference": "ABC00001", "amounts": [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], "bacs_reference": "", "start_from": "2015-01-01", "roll_status": "Y", "installments": 12, "service_description": "Gym Membership"}}')

#  Update Direct Debits
	def test_updateDirectDebit(self):
		dfcapi.setUpdateDirectDebitUrl('http://httpbin.org/post')
		response = dfcapi.UpdateDirectDebit('TEST-TEST-TEST-TEST','fee78bd3bf59bfb36238b3f67de0a6ea103de130','000101AA0001','','','','','','','','','','','','','','','','','15','012015','','','','','')				
		self.assertEqual(response.code, 200)
		self.assertEqual(response.body['data'], '{"payer": {"birth_date": "", "first_name": "", "last_name": "", "title": ""}, "general": {"installmentamount": "", "newamount": "", "applyfrom_paydate": "012015", "applyfrom": "", "paymentdate": "15", "yourref": "", "latepayment": "", "installmentduedate": ""}, "authentication": {"dfc_ref": "000101AA0001", "apikey": "TEST-TEST-TEST-TEST", "apisecret": "fee78bd3bf59bfb36238b3f67de0a6ea103de130"}, "contact": {"mobile": "", "phone": "", "email": ""}, "address": {"town": "", "address1": "", "address2": "", "address3": "", "county": "", "postcode": ""}, "bank": {"sort_code": "", "account_number": ""}}')
# Cancel Direct debits
	def test_cancelDirectDebit(self):
		dfcapi.setCancelDirectDebitUrl('http://httpbin.org/post')
		response = dfcapi.CancelDirectDebit('TEST-TEST-TEST-TEST','fee78bd3bf59bfb36238b3f67de0a6ea103de130','000101AA0001','2015-01-01')			
		self.assertEqual(response.code, 200)
		self.assertEqual(response.body['data'], '{"cancel": {"apply_from": "2015-01-01"}, "authentication": {"dfc_ref": "000101AA0001", "apikey": "TEST-TEST-TEST-TEST", "apisecret": "fee78bd3bf59bfb36238b3f67de0a6ea103de130"}}' )


if __name__ == '__main__':
	unittest.main()

# -*- coding:utf-8 -*-

import sys
import os
import unittest


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import unirest
#from inspect import getmembers
from pprint import pprint
from array import *
import json

api_url_checkkey          = 'https://api.debitfinance.co.uk/checkkey'
api_url_viewdd 		      = 'https://api.debitfinance.co.uk/viewdd'
api_url_viewdd_breakdown  = 'https://api.debitfinance.co.uk/viewddbreakdown'
api_url_createDirectDebit = 'https://api.debitfinance.co.uk/setupdd'
api_url_updateDirectDebit = 'https://api.debitfinance.co.uk/updatedd'
api_url_cancelDirectDebit = 'https://api.debitfinance.co.uk/canceldd'

#class dfcapi:


#setCheckKeyUrl
def setCheckKeyUrl(checkkey_url):
	global api_url_checkkey 
	api_url_checkkey = checkkey_url
#setCheckKeyUrl
def setViewDirectDebitUrl(viewdd_url):
	global api_url_viewdd
	api_url_viewdd = viewdd_url
#setCheckKeyUrl
def setViewDirectDebitBreakdownUrl(viewdd_bd_url):
	global api_url_viewdd_breakdown
	api_url_viewdd_breakdown = viewdd_bd_url
#setCheckKeyUrl
def setCreateDirectDebitUrl(setupdd):
	global api_url_createDirectDebit
	api_url_createDirectDebit = setupdd
#setCheckKeyUrl
def setUpdateDirectDebitUrl(updatedd):
	global api_url_updateDirectDebit
	api_url_updateDirectDebit = updatedd
#setCheckKeyUrl
def setCancelDirectDebitUrl(cancelldd):
	global api_url_cancelDirectDebit
	api_url_cancelDirectDebit = cancelldd

#  Checkey
def checkApiKey(api_key,api_secret):
	response = unirest.get(api_url_checkkey, auth=(api_key,api_secret))
	return response
#  View Direct Debits
def ViewDirectDebits(api_key,api_secret,dfc_ref):
	response = unirest.get(api_url_viewdd,  params={"dfc_reference":dfc_ref},  auth=(api_key,api_secret)) 
	return response
#  View Direct Debits Breakdown
def ViewDirectDebitsBreakdown(api_key,api_secret,dfc_ref):
	response = unirest.get(api_url_viewdd_breakdown,  params={"dfc_reference":dfc_ref},  auth=(api_key,api_secret)) 
	return response
#  Create Direct Debits  
def createDirectDebit(api_key,api_secret,client_reference,reference,title,first_name,last_name,address1,address2,address3,town,county,postcode,amounts,email,account_number,sort_code,start_from,installments,frequency_unit,frequency_type,roll_status,birth_date,mobile_number,phone_number,no_email,service_description,bacs_reference,skip_check):
	authentication = {"apikey": api_key, "apisecret": api_secret, 'club_ref_no':client_reference}
	payer		   = {'title':title,'first_name':first_name,'last_name':last_name, 'birth_date':birth_date}
	address 	   = {'address1':address1,'address2':address2,'address3':address3,'town':town,'county':county,'postcode':postcode, 'skip_check':skip_check}
	contact		   = {'email':email,'mobile_number':mobile_number,'phone_number':phone_number,'no_email':no_email}
	bank		   = {"account_number": account_number, "sort_code": sort_code}
	subscription   = {'reference':reference,'service_description':service_description,'start_from':start_from,'amounts':amounts,'installments':installments,'bacs_reference':'','roll_status':roll_status}

	response = unirest.post(api_url_createDirectDebit, headers={ "Accept": "application/json", "Content-Type": "application/json" }, params=json.dumps({'authentication':authentication, 'payer':payer,'address':address,'contact':contact,'bank':bank,'subscription':subscription}) )
	return response
#  Update Direct Debits  
def UpdateDirectDebit(api_key,api_secret,dfc_ref,reference,title,first_name,last_name,address1,address2,address3,town,county,postcode,email,account_number,sort_code,birth_date,mobile_number,phone_number,paymentdate,applyfrom_paydate,installmentduedate,installmentamount, latepayment, applyfrom,newamount):
	authentication = {"apikey": api_key, "apisecret": api_secret, 'dfc_ref':dfc_ref}
	payer		   = {'title':title,'first_name':first_name,'last_name':last_name, 'birth_date':birth_date}
	address 	   = {'address1':address1,'address2':address2,'address3':address3,'town':town,'county':county,'postcode':postcode}
	contact		   = {'phone':phone_number,  'mobile':mobile_number, 'email':email}
	bank		   = {"account_number": account_number, "sort_code": sort_code}
	general        = {'yourref':reference,'paymentdate':paymentdate,'installmentduedate':installmentduedate,'installmentamount':installmentamount,'latepayment':latepayment,'applyfrom':applyfrom,'applyfrom_paydate':applyfrom_paydate,'newamount':newamount}
	
	response = unirest.post(api_url_updateDirectDebit, headers={ "Accept": "application/json", "Content-Type": "application/json" }, params=json.dumps({'authentication':authentication, 'payer':payer,'address':address,'contact':contact,'bank':bank, 'general':general}) )
	return response
#  Cancel Direct Debits
def CancelDirectDebit(api_key,api_secret,dfc_ref,apply_from):
	authentication = {"apikey": api_key, "apisecret": api_secret, 'dfc_ref':dfc_ref}
	cancel		   = {'apply_from':apply_from}
	response = unirest.post(api_url_cancelDirectDebit, headers={ "Accept": "application/json", "Content-Type": "application/json" }, params=json.dumps({'authentication':authentication, 'cancel':cancel}) )
	return response

 


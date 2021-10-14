#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# --------------------------------------------------------
#
__author__      = "Thomas Sterber"
__copyright__   = "October 2021"
__license__     = "GPL"
__email__       = "thomas.sterber@meraki.net"
__status__      = "demo"





# --------------------------------------------------------
# Import Modules
# --------------------------------------------------------
#
import time, os, sys, json
import warnings
#
try:
	from requests.packages.urllib3 import exceptions
	import requests
except:
	os.system('pip3 install requests')
	time.sleep(2)
	from requests.packages.urllib3 import exceptions
	import requests



# --------------------------------------------------------
# static variablen
# --------------------------------------------------------
#
api_url = 'https://api.meraki.com/api/v1'
line = 80*'-'



infotext = """

                                 ./(((((((((((((((((/.
                            *(((((((((((((((((((((((((((((
                         .(((((((((((((((((((((((((((((((((((/
                       ((((((((((((((((((((((((((((((((((((((((/
                     ,((((((((((((((((((((((((((((((((((((((((((((
                   .((((((((((((((((((((     ((((((/     ((((((((((,
                  ((((((((((((((((((((((     ((((((/     (((((((((((
               /((((((((((((((((((((((((((((((((((((((((((((((((((((
              ((((((((((((((((((((((((((((((((((((((((((((((((((((((*
             ((((((((((((((((((((((((((((((((((((((((((((((((((((((((
            (((((((((((((((((((((((((((((((((((((((((((((((((((((((((
           ((((((((((((((((((((((((     ((((((((((((((/     (((((((((
          ,((((((((((((((((((((((((     ((((((((((((((/     ((((((((/
          (((((((((((((((((((((((((    .//////////////*    .((((((((
         ,(((((((((((((((((((((((((((((/              ((((((((((((.
         ((((((((((((((((((((((((((((((/              (((((((((((
         (((((((((((((((((((((((((((((((((((((((((((((((((((((((*
        .(((((((((((((((((((((((((((((((((((((((((((((((((((((*
        /((((((((((((((((((((((((((((((((((((((((((((((((((*
        (((((((((((((((((((((((((((((((((((((((((((((((*
        (((((((((((/.                     ....
        (((((((/
        (((((
        (((
        /.            Welcome to the power of the Meraki API


    This is a demo on how to manage custom Webhook-payloadTemplates
    If you like to upload your custom Webhook-payloadTemplate,
    the headers.liquid and body.liquid file needs to be in the same dir as this script.

              The use of this tool is on your own risk.

    Please visit:  https://meraki.io

"""

# -----------------------------------------------
#  Functions
# -----------------------------------------------
def select_org():
	"""get orgid's for given accesstoken and select one"""
	#
	url = api_url + '/organizations'
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	orgas = response.json()
	# print(json.dumps(orgas, sort_keys=True, indent=4))
	#
	print('\n')
	dic = {}
	count=0
	for n in orgas:
		orgname = str(n['name'])
		orgid    = str(n['id'])
		print(str(count).rjust(3,' '),'   ', orgname.ljust(20, ' '), orgid)
		dic[count] = orgid
		count += 1
	print('\n')
	select = input('select org  >')
	organizationId = dic[int(select)]
	#
	return(organizationId)



def select_network(organizationId):
	""" get all networks of organizationId and select one"""
	#
	resource = f'/organizations/{organizationId}/networks'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	# print(json.dumps(re, sort_keys=True, indent=4))
	#
	dic = {}
	count=0
	for n in re:
		networkname = str(n['name'])
		networkId    = str(n['id'])
		print(str(count).rjust(3,' '),'   ', networkname.ljust(20, ' '), networkId)
		dic[count] = networkId
		count += 1
	print('\n')
	select = input('select network  >')
	# print(dic)
	# print(dic[int(select)])
	networkId = dic[int(select)]
	#
	return(networkId)


def end():
	""" end script """
	sys.exit()


def list_all_payloadTemplates():
	""" get all payloadTemplates of network """
	#
	resource = f'/networks/{networkId}/webhooks/payloadTemplates'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	# print(json.dumps(re, sort_keys=True, indent=4))
	print(line)
	count=0
	for n in re:
		payloadTemplateName = str(n['name'])
		payloadTemplateId   = str(n['payloadTemplateId'])
		payloadTemplateType = str(n["type"])
		print(str(count).rjust(3,' '),'   ', payloadTemplateName.ljust(20, ' '), payloadTemplateId.ljust(20, ' '), payloadTemplateType)
		count += 1
	print(line)
	#
	return()


def list_all_included_payloadTemplates():
	""" get all payloadTemplates of the network """
	#
	resource = f'/networks/{networkId}/webhooks/payloadTemplates'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	# print(json.dumps(re, sort_keys=True, indent=4))
	print(line)
	count=0
	for n in re:
		if str(n["type"]) == "included":
			payloadTemplateName = str(n['name'])
			payloadTemplateId   = str(n['payloadTemplateId'])
			payloadTemplateType = str(n["type"])
			print(str(count).rjust(3,' '),'   ', payloadTemplateName.ljust(20, ' '), payloadTemplateId)
			count += 1
	print(line)
	#
	return()


def list_all_custom_payloadTemplates():
	""" get all payloadTemplates of the network """
	#
	resource = f'/networks/{networkId}/webhooks/payloadTemplates'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	# print(json.dumps(re, sort_keys=True, indent=4))
	print(line)
	count=0
	for n in re:
		if str(n["type"]) == "custom":
			payloadTemplateName = str(n['name'])
			payloadTemplateId   = str(n['payloadTemplateId'])
			payloadTemplateType = str(n["type"])
			print(str(count).rjust(3,' '),'   ', payloadTemplateName.ljust(20, ' '), payloadTemplateId)
			count += 1
	print(line)
	#
	return()


def select_a_payloadTemplate():
	""" get a payloadTemplate of the network """
	#
	resource = f'/networks/{networkId}/webhooks/payloadTemplates'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	# print(json.dumps(re, sort_keys=True, indent=4))
	#
	dic = {}			# {count:'id'} create dic
	count=0
	for n in re:
		payloadTemplateName = str(n['name'])
		payloadTemplateId   = str(n['payloadTemplateId'])
		payloadTemplateType = str(n["type"])
		print(str(count).rjust(3,' '),'   ', payloadTemplateName.ljust(20, ' '), payloadTemplateId)
		dic[count] = payloadTemplateId
		count += 1
	print('\n')
	select = input('select template  >')
	payloadTemplateId = dic[int(select)]
	#
	return(payloadTemplateId)



def display_a_payloadTemplate():
	""" display a selected payloadTemplate """
	#
	# select payloadTemplate
	payloadTemplateId = select_a_payloadTemplate()
	#
	resource = f'/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	# print(json.dumps(re, sort_keys=True, indent=4))
	#
	os.system('clear')  # clear screen
	print(line)
	name = re['name']
	print(f"Template '{name}' content :")
	print(line)
	for key in re:
		print('\n')
		print(key)
		print('---------------------')
		print(re[key])
	print(line)
	#
	return()


def select_a_custom_payloadTemplate():
	""" get custom payloadTemplates of the network """
	#
	resource = f'/networks/{networkId}/webhooks/payloadTemplates'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	# print(json.dumps(re, sort_keys=True, indent=4))
	#
	dic = {}			# {count:'id'} create dic
	count=0
	for n in re:
		if str(n["type"]) == "custom":
			payloadTemplateName = str(n['name'])
			payloadTemplateId   = str(n['payloadTemplateId'])
			payloadTemplateType = str(n["type"])
			print(str(count).rjust(3,' '),'   ', payloadTemplateName.ljust(20, ' '), payloadTemplateId)
			dic[count] = payloadTemplateId
			count += 1
	print('\n')
	select = input('select template  >')
	# print(dic)
	# print(dic[int(select)])
	payloadTemplateId = dic[int(select)]
	#
	return(payloadTemplateId)


def delete_a_custom_payloadTemplate():
	""" delete a selected payloadTemplate """
	#
	# select custom payloadTemplate
	payloadTemplateId = select_a_custom_payloadTemplate()
	#
	# delete payloadTemplateId in network
	resource = f'/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}'
	url = api_url + resource
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.delete(url, headers=headers, verify=False)
	print('Status_code : ', response.status_code)
	print('Status_text : ', response.text)
	#
	return()


def display_webhooks_alert_types():
	""" download and display actual webhook alert types """
	#
	url = api_url + f'/organizations/{organizationId}/webhooks/alertTypes'
	#
	headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.get(url, headers=headers, verify=False)
	re = response.json()
	data = json.dumps(re, sort_keys=True, indent=4)
	# display alert types
	print(data)
	# save re to file
	print ("result will be stored in 'webhook_alert_types.txt'")
	f = open('webhook_alert_types.txt', 'w')
	f.write(data)
	f.close
	print("done")
	#
	return()


def upload_a_custom_payloadTemplate():
	""" upload custom payloadTemplate """
	#
	# read *.liquid files in working dir
	dirlist = os. listdir()
	#print (dirlist)
	#
	# select headers.liquid file
	dic = {}
	count=0
	print('\n')
	for filename in dirlist:
		#print(filename)
		if (filename[-14:] == "headers.liquid"):
			print(str(count).rjust(3,' '),'   ', filename)
			dic[count] = filename
			count += 1
	print('\n')
	select = input('select headers.liquid file  >')
	header_file = dic[int(select)]
	#
	# select body.liquid file
	dic = {}
	count=0
	print('\n')
	for filename in dirlist:
		if (filename[-11:] == "body.liquid"):
			print(str(count).rjust(3,' '),'   ', filename)
			dic[count] = filename
			count += 1
	print('\n')
	select = input('select body.liquid file  >')
	body_file = dic[int(select)]
	#
	print(line)
	print('selected files: \n')
	print('\tHeader file :', header_file)
	print('\tBody file   :', body_file)
	check = input('\nPress Enter to upload')
	#
	# upload payloadTemplate
	resource = f'/networks/{networkId}/webhooks/payloadTemplates'
	url = api_url + resource
	#
	webhook_name = input('template_name :')
	payload={'name': webhook_name}
	#
	files = [
			('headersFile', ('customTemplate.headers.liquid', open(header_file, 'rb'),'application/octet-stream')),
			('bodyFile', ('customTemplate.body.liquid', open(body_file,'rb'),'application/octet-stream'))
			]
	#
	# headers = {'X-Cisco-Meraki-API-Key': accesstoken, 'Content-Type': 'application/json'}
	headers = {'X-Cisco-Meraki-API-Key': accesstoken}   # !! Content type
	warnings.simplefilter("ignore", exceptions.InsecureRequestWarning)
	response = requests.post(url, headers=headers, data=payload, files=files, verify=False)
	print('response code : ' , response.status_code)
	print('response text : ' , response.text)
	#
	return()



# Action Menue
def get_action():
	# os.system('clear')       # clear screen
	breite = 55
	rahmenh = '#'
	rahmenv = '|'
	menue = [
			['list_all_payloadTemplates', list_all_payloadTemplates],
			['list_all_custom_payloadTemplates', list_all_custom_payloadTemplates],
			['list_all_included_payloadTemplates', list_all_included_payloadTemplates],
			['display_a_payloadTemplate', display_a_payloadTemplate],
			['display_webhooks_alert_types', display_webhooks_alert_types],
			['upload_a_custom_payloadTemplate', upload_a_custom_payloadTemplate],
			['delete_a_custom_payloadTemplate', delete_a_custom_payloadTemplate],
			['quit', end]
			]
	print ('\n\n   What do you like to do ? ')
	print(breite * '-')

	count = 0
	for element in menue:
		element = '    ' + element[0]
		print (rahmenv + ' '.ljust(breite,' ') + rahmenv)
		print (rahmenv + ' ' + str(count).ljust(4,' ') + ' ' + element.ljust(breite-6,' ') + rahmenv)
		print (rahmenv + ' '.ljust(breite,' ') + rahmenv)
		count +=1
	print (''.ljust(breite + 2,rahmenh))
	select = int(input (' >> '))
	try:
		action = menue[select][1]
		return (action)
	except:
		return("error")




#
# --------------------------------------------------------
# Main
# --------------------------------------------------------
#
if __name__ == "__main__":
	#workdir          = os.path.abspath(os.curdir)
	#
	os.system('clear')  # clear screen
	print(infotext)
	input('\n\tPress Enter to continue')
	os.system('clear')  # clear screen
	#
	# init
	workdir          = os.path.abspath(os.curdir)
	accesstoken      = input("\nAPI Token : ")
	os.system('clear')  # clear screen
	organizationId   = select_org()
	networkId        = select_network(organizationId)
	os.system('clear')  # clear screen
	#
	# action menue
	endlosschleife = True
	while endlosschleife:
		os.system('clear')       # clear screen
		aktion = get_action()
		if aktion == "error":
			print("input error")
			time.sleep(2)
			continue
		aktion()
		wait = input('Press Enter to continue')

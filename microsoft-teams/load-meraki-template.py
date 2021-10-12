#!/usr/bin/env python3
#
# load-meraki-template.py lets you load a template into the Cisco Meraki Dashboard that
# allows alerts to be sent as webhooks to a Microsoft Teams channel.
#
# Installation:
# load-meraki-template.py uses dotenv to safely store your credentials.  Create a file called .meraki.env
# in your home directory.  For Linux this is typically /home/username.  For Windows this
# is typically
# c:\users\<username>.
# Into .meraki.env put this line:
# x_cisco_meraki_api_key=<your API key>
# If you don't have an API key yet then follow the instructions on this page:
# https://documentation.meraki.com/zGeneral_Administration/Other_Topics/The_Cisco_Meraki_Dashboard_API
#
# Prior to running this script you'll need Python 3.x installed and you'll need to run the below
# commands to install the extra components required.
# pip3 install -U meraki
# pip3 install -U python-dotenv
#
# Edit orgName and netName with the name of your organisation and network to load the template into.
#
#
# References:
# https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook
# https://developer.cisco.com/meraki/webhooks/#!custom-templates/custom-payload-templates
# https://docs.microsoft.com/en-us/outlook/actionable-messages/send-via-connectors
# https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL
# https://github.com/meraki/webhook-payload-templates
# https://webhook-builder-vpfmunhy6a-uc.a.run.app/
#

import os,meraki,requests,json

# Update these for your org and network name
orgName="IFM NZ Ltd"
netName="IFM-Office"

# The name of this template
templateName="Microsoft Teams"

# Load global and local Cisco Meraki settings such as x_cisco_meraki_api_key
from dotenv import load_dotenv
load_dotenv()
load_dotenv(dotenv_path=os.path.join(os.path.expanduser("~"),".meraki.env"))

# You can define the API key here, put it in .meraki.env or put it in the environment
apiKey=os.getenv("x_cisco_meraki_api_key")

dashboard = meraki.DashboardAPI(
	api_key=apiKey,
	suppress_logging=True
)


# This function retrieves the netId given an org name and a net name
def getNetId(orgName,netName):
	orgId=None
	netId=None

	# Search for the org
	for org in dashboard.organizations.getOrganizations():
		if org['name'] == orgName:
			orgId=org['id']
			break;

	if orgId == None:
		print("Invalid organization name supplied: "+orgName)			
		exit(-1)

	# Search for the network
	for net in dashboard.organizations.getOrganizationNetworks(orgId):
		if net['name'] == netName:
			netId=net['id']
			break;

	if netId == None:
		print("Invalid network name supplied: "+netName)			
		exit(-1)

	return netId


def main():
	# Build the URL to the REST endpoint
	url = f"https://api.meraki.com/api/v1/networks/{getNetId(orgName,netName)}/webhooks/payloadTemplates"

	headers = {
		'X-Cisco-Meraki-API-Key' : apiKey,
#		'Content-Type': 'application/json'
	}

	# Delete existing template
	print(f"Attempting to delete {templateName}")
	response = requests.request("GET", url, headers=headers)
	for template in response.json():
		if(template['name'] == templateName):
			try:
				response=requests.request("DELETE", url+"/"+template['payloadTemplateId'], headers=headers)

				# Check if the template is already referenced
				if response.status_code == 400:
					print(response.text)
					print("This needs to be changed before the template can be added again.")
					exit(-1)

				# If some other kind of error try and continue on
				if response.status_code != 200:
					print(response.text)
			except requests.exceptions.RequestException as e:
				print(e)

	# Upload the new template
	print(f"Attempting to add {templateName}")
	payload={'name': templateName}
	files=[('headersFile',('headers.liquid',open('headers.liquid','rb'),'application/octet-stream')),('bodyFile',('body.liquid',open('body.liquid','rb'),'application/octet-stream'))]

	try:
		response = requests.request("POST", url, headers=headers, data=payload, files=files)
		if response.status_code != 201:
			print(response.text)
	except requests.exceptions.RequestException as e:
		print(e)


if __name__ == "__main__":
	# Execute only if run as a script
	main()

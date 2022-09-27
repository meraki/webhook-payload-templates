## ServiceNow

Enables the [ServiceGraph Connector for Meraki](https://meraki.io/build/servicenow) to receive webhooks and generate incidents. 

This template supports the required authentication headers and password complexity implemented with the San Diego release of ServiceNow.

<img src="servicenow-incident-screenshot.png" alt="meraki default JSON" width="600">

The ServiceNow connector relies on Basic authentication to send a webhook to the service.

The setup required that the Meraki admin set the HTTPS Server URL to the following format.

`https://username:passwordk@venXXXX.service-now.com/api/x_caci_sg_meraki/sgmeraki_device_alerts`

However, with the ServiceNow San Diego relese, passwords are automatically defined for you and are too complex for embeding in the URL. 

This resulted in an incompatible URL

`https://MerakiAlerts:::_4KNFuh@#$%&_nkdsjfn234^6@@venXXXX.service-now.com/api/x_caci_sg_meraki/sgmeraki_device_alerts`

To solve this, 
Instead of encoding the `username:password` in the URL as before, with templates we can now use headers to send the credentials. 

```
"Authorization":"Basic {{sharedSecret | base64_encode}}"
```

### Meraki Dashboard Webhook

- **httpServer URL**: https://venXXXX.service-now.com/api/x_caci_sg_meraki/sgmeraki_device_alerts
- **sharedSecret**: `username:password`






<hr>

### Template 

- [headers.liquid](headers.liquid)
- [body.liquid](body.liquid)

**headers.liquid**

```liquid 'headers.liquid'
{
    "Authorization":"Basic {{sharedSecret | base64_encode}}"
}
```


**body.liquid**

```liquid 'body.liquid'


```json result
{
    "sentAt": "2021-05-11T08:09:00.072534Z",
    "organizationId": "2930418",
    "organizationName": "My organization",
    "organizationUrl": "https://dashboard.meraki.com/o/VjjsAd/manage/organization/overview",
    "networkId": "N_24329156",
    "networkName": "Main Office",
    "networkUrl": "https://n1.meraki.com//n//manage/nodes/list",
    "networkTags": ["region-1","corporate"],
    "deviceSerial": "Q234-ABCD-5678",
    "deviceMac": "00:11:22:33:44:55",
    "deviceName": "My AP",
    "deviceUrl": "https://n1.meraki.com//n//manage/nodes/new_list/000000000000",
    "deviceTags": ["tag1","tag2"],
    "deviceModel": "MR34",
    "alertId": "0000000000000000",
    "alertType": "VPN connectivity changed",
    "alertTypeId": "vpn_connectivity_change",
    "alertLevel": "warning",
    "occurredAt": "2018-02-11T00:00:00.123450Z",
    "alertData": {"vpnType":"l2tpv3","vap":"1","onSecondary":false,"secondaryEndpoint":"192.168.1.2","primaryEndpoint":"192.168.1.1","connectivity":"true","peerNetworkName":"Corp Access","peerNetworkUrl":"https://n1.meraki.com//n//manage/nodes/list","peerNetworkId":"N_24329156"}
}
    
```
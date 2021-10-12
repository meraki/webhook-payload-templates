## Microsoft Teams

[API Docs](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/connectors-using?tabs=cURL)

Post a webhook alert into a Microsoft Teams channel.

<img src="motion-alert-screenshot.jpg" alt="Motion alert" width="500">
<img src="power-supply-screenshot.jpg" alt="Power supply alert" width="500">

<hr>

You will first need to [WebHook enable the channel](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook).
This process creates the HTTP server URL to enter into the Meraki Dashboard.

Next run the [load-meraki-template.py](load-meraki-template.py) Python script to load the template into the Cisco Meraki Dashboard.

### Template 

- [headers.liquid](headers.liquid)
- [body.liquid](body.liquid)
- HTTP Server URL: `https://your-domain.atlassian.net/rest/api/2/issue/createmeta`


```headers.liquid
{
}
```
```body.liquid
{
	"@type": "MessageCard",
	"@context": "https://schema.org/extensions",
	"summary": "{{organizationName}}",

	"sections": [{
		"activityTitle": "{{organizationName}}",
		"activitySubtitle": "{{networkName}}",
		{% if alertData.imageUrl %}"images": [{"image":"{{alertData.imageUrl}}"}],{% endif %}
		"facts": [
    {
			"name": "When",
			"value": "{{occurredAt}}"
    },
		{
			"name": "Device",
			"value": "{{deviceName}}"
		},
		{
			"name": "Alert",
			"value": "{{alertType}} - {{alertLevel}}"
    }{% unless alertData.imageUrl %},
    {
			"name": "",
			"value": "{{alertData | json_markdown}}"
    }{% endunless %}],
    "markdown": true
  }],
	"potentialAction": [{
		"@type": "OpenUri",
		"name": "Org",
		"targets": [{"os": "default", "uri" : "{{organizationUrl}}"}]
	},
	{
		"@type": "OpenUri",
		"name": "Network",
		"targets": [{"os": "default", "uri" : "{{networkUrl}}"}]
	},
	{
		"@type": "OpenUri",
		"name": "Device",
		"targets": [{"os": "default", "uri" : "{{deviceUrl}}"}]
	}]
}
```
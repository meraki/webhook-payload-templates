## DataDog 

[API Docs](https://docs.datadoghq.com/api/latest/events/)

Log an event in DataDog.

<img src="custom-template-datadog-example.png" alt="DataDog" width="500" />

<hr>

### Template 

- [body.liquid](body.liquid)
- [headers.liquid](headers.liquid)
- HTTP Server URL: 
    - https://api.datadoghq.eu/api/v1/events
    - https://api.datadoghq.com/api/v1/events

```body.liquid
{
    "payload": {
        "summary": "{{alertType}}",
        "timestamp": "{{occurredAt}}",
        "source": "{{networkId}}",
        "organizationId": "{{organizationId}}",
        "severity": "{% if alertLevel == 'informational' %}info{% else %}warning{% endif %}",
        "component": "{{deviceName}}",
        "group": "{{networkName}}",
        "class": "deploy",
        "custom_details": "{{alertData | jsonify | escape}}"
    },
    "routing_key": "{{sharedSecret}}",
    "dedup_key": "{{alertId}}",
    "images": [
        {
            "src": "{{alertData.imageUrl}}",
            "href": "{{alertData.imageUrl}}",
            "alt": "Image"
        }
    ],
    "links": [
        {
            "href": "{{deviceUrl}}",
            "text": "Device"
        },
        {
            "href": "{{networkUrl}}",
            "text": "Network"
        },
        {
            "href": "{{organizationUrl}}",
            "text": "Organization"
        }
    ],
    "event_action": "trigger",
    "client": "Manage Meraki Device",
    "client_url": "{{deviceUrl}}"
}

```
```headers.liquid
{
    "DD-API-KEY":"{{sharedSecret}}"
}
```
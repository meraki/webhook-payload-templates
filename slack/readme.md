## Slack 

Send a message to a Slack channel

[API Docs - Incoming Webhooks](https://api.slack.com/messaging/webhooks)

<img src="custom-template-slack-screenshot.png" alt="image_tooltip" width="500"/>

### Template 

- [body.liquid](body.liquid)

- HTTP Server URL: `https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX`

```body.liquid
{% capture markdown %}
Alert ID: {{alertId}}
Alert level: {{alertLevel}}
Occurred at: {{occurredAt}}
Alert data: {{alertData | json_markdown}}
{% endcapture %}
{
    "text": "{{alertType}}",
    "blocks": [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "{{alertType}}"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": {{markdown | jsonify}}
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Organization name: *<{{organizationUrl}}|{{organizationName}}>*\nOrganization ID: {{organizationId}}\n"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Network name: *<{{networkUrl}}|{{networkName}}>*\nNetwork ID: {{networkId}}\n"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Device name: {{deviceName}}\nDevice serial: <{{deviceUrl}}|{{deviceSerial}}>\nDevice MAC: {{deviceMac}}\nDevice tags: {{deviceTags | join: ', '}}\nDevice model: {{deviceModel}}\n"
            }
        }
    ],
    "organizationId": "{{organizationId}}",
    "networkId": "{{networkId}}"
}
```
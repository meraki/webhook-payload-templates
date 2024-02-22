## Cisco XDR Automation

[Documentation for Cisco XDR Automation Webhooks](https://docs.xdr.security.cisco.com/Content/Automate/webhooks.htm)

This document describes how to trigger one or more Automation Workflows with an Automation Rule in Cisco XDR.

To use webhooks in Cisco XDR Automation, you must create the Webhook, create an Automation Rule with it, associate one or more Workflows, and add an Activity to the Workflow that executes when it's triggered. The incoming Meraki webhook will cause the Automation Rule to trigger the Workflow. This Workflow can then use the body of the Meraki Alert to do any desired outcomes.

> **Note:** An external event can trigger a workflow 5 times within 1 minute. This threshold is set for each trigger individually. When this limit is reached, any unprocessed events will roll over to be processed in the next minute.

### Create a Webhook in Cisco XDR Automation
When you create a webhook, you will be given an HTTP endpoint where you can push events from the source product:

1. In the Cisco XDR UI, choose **Automate > Triggers** in the navigation menu.
2. Click the **Webhooks** tab and then click **New Webhook**.
3. In the **General** section, enter the following information:
- **Display Name** - A unique meaningful name for the webhook (e.g. "Meraki Webhook").
- **Description** - Text that describes the webhook, such as what the incoming data will trigger.
- **Request Content Type** - Click the drop-down list and choose the following Content-Type for your payload (incoming webhook): `application/json`.
4. Click **Submit** to create the webhook. The newly created webhook is displayed at the top of the list on the Webhooks tab.
6. In the **Display name** column on the **Webhooks** tab, click the webhook to view the generated Webhook ID, AO API Key, and Webhook URL. Copy paste this URL, as you need it in the Meraki Dashboard later.
7. You can now go to the **Automation Rules** tab and create a Webhook rule to listen for incoming data from the webhook. This rule will be used as a trigger to execute the associated workflow.

### Template

- HTTP Server URL: `<YOUR FULL XDR WEBHOOK URL>`
- Body: [body.liquid](body.liquid) (simply the raw Meraki Alert JSON)
- Headers: [headers.liquid](headers.liquid) (`"Content-Type":"application/json"`)
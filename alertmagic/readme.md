# AlertMagic

<img src="AlertMagicLogo.png" alt="image_tooltip" width="600" />

AlertMagic avoids ticket duplicates, performs smart field mappings and can perform complex logic on incoming Meraki webhooks.
Effectively and efficiently create/update incidents and problems in AutoTask, Jira, ServiceNow, ZenDesk and more.

More information at the [AlertMagic Website](https://www.panoramicdata.com/products/alertmagic/)

<hr>

### Template

- [header.liquid](header.liquid)
- [body.liquid](body.liquid)
- HTTP Server URLs:
    * `pdl-alertmagic.azurewebsites.net/api/notify` (production system)
    * `pdl-alertmagic-staging.azurewebsites.net/api/notify` (test/staging system)
- Shared secret:
    * Should be in the form `Basic Base64EncodedUsernameAndPassword`

<hr>
Creating your shared secret...

Let's say your AlertMagic username and password are MYUSERNAME and MYPASSWORD

1. Construct the string `MYUSERNAME:MYPASSWORD`, with a colon separating the two
1. Find a trusted Base 64 encoding system (there are a few on the web, for example: https://www.base64encode.org/)
1. Get the Base 64 encoded version (in this case `TVlVU0VSTkFNRTpNWVBBU1NXT1JE`)
1. Use this in your shared secret as follows: `Basic TVlVU0VSTkFNRTpNWVBBU1NXT1JE`
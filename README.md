# PalsSign
Pull the daily saying from Palsweb.com and send it to a text number.

This needs to be called with the address you are sending to as a command line argument. For example: palsign.py john.doe@example.com.

While you should be able to pass multiple email addresses to the script, it hasn't been working as expected. And, since the original author wants to use this as a cronjob to send the saying to various people, it is easy to set up multiple cron entries with a different address to send to.

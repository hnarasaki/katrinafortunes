Katrina Fortunes
========
![katrina](/katrina2.png)

Katrina Fortunes sends fortunes from Animal Crossing's beloved fortune-teller Katrina vis SMS using the Twilio API.

This project was forked from catfacts by 0x27.

# What?
Katrina Fortunes is a simple SMS sending tool that iterates over a list of messages to send and sends them with a random delay between messages, ranging from 5 minutes to an hour.

It was inspired by the hilarious "catfacts" prank and is intended to facilitate such lulz.

# How?
Enter credentials from your Twilio account. You can find these in your Twilio Developer Console.

sender = Your Twilio phone number in e.164 format. 
Ex: "+11234567890"

account_sid = Your Twilio account_sid.

auth_token = Your Twilio auth_token.

# Setup
Run `pip install twilio==5.7.0` to install version 5.7 of the Twilio helper library.

# Running Katrinafortunes
To run Katrinafortunes, run 
`python katrinafortunes.py <your Twilio number here>`
Ex: `python katrinafortunes.py +11234567890`

You should see a response like the following:
{+} Launching katrinafortunes against +11234567890
{+} Sending Message!
{*} Message sent!
{+} Sleeping for 2947

# Todo
Support the latest version of the Twilio helper library. https://www.twilio.com/docs/libraries/python

# Licence
Licenced under the ["wtfpl license."][wtfpl]

[wtfpl]: http://wtfpl.net/

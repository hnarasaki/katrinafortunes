#!/usr/bin/python2
# coding: utf-8
# katrinafortunes - Sends an Animal Crossing Katrina fortune via SMS.
# Forked from catfacts repo by ~0x27
# TODO: Write a reply handling thread with automatically generated

import random
import sys
import time

from twilio.rest import TwilioRestClient

# Global variables. Update these with your Twilio credentials...
sender = "+11234567890"
account_sid = "XXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXX"

def send_sms(phone, message):
    client = TwilioRestClient(account_sid, auth_token)
    message = client.messages.create(to=phone, from_=sender, body=message)
    print("{*} Message sent!")
    
def katrina_fortunes(recipient):
    print("{+} Launching katrinafortunes against %s" % (recipient))
    try:
        for line in open("fortune_list.txt").readlines():
            print("{+} Sending Message!")
            try:
                send_sms(phone=recipient, message=line)
            except Exception:
                print("{!} There was an error sending your message!")
                pass
            wait_time = random.randint(300, 3600)
            print("{+} Sleeping for %d" %(wait_time))
            time.sleep(wait_time)
        print("{+} Katrinafortunes expended!")
    except KeyboardInterrupt:
        sys.exit("{-} Katrinafortunes Terminated!")
        
def main(args):
    if len(args) != 2:
        sys.exit("use: %s <recipientphone>" %(args[0]))
    katrina_fortunes(recipient=args[1])

if __name__ == "__main__":
    main(args=sys.argv)

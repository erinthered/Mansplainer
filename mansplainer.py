#!/usr/bin/python

import os
from clarifai.client import ClarifaiApi

#Clarifai keys
os.environ["CLARIFAI_APP_ID"]="T6ZF_EuGDplxDhLUk2qtkCvEJdn_lT_usf00zAWc"
os.environ["CLARIFAI_APP_SECRET"]="clwcHLrrami5VJj2PzIGSc7tiwFUGbTsP8Fg0HDd"
api = ClarifaiApi()  # assumes environment variables are set.

from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import Client

account_sid = "ACbe0730baeb75b5f6a870f65bfabe386d"
auth_token = "0d08cdad7424c231bc1f34a6b3456777"
client = Client(account_sid, auth_token)

app = Flask(__name__)

#list of phone numbers of winners of scavenger hunt
winnerList = []

#global counter to keep track of number of winner slots available
winnerCounter = 3

def get_winner():
    global winnerCounter
    return(winnerCounter)

    def set_winner(winner):
        global winnerCounter
        winnerCounter = winner

        @app.route("/", methods=['GET', 'POST'])

        def incoming_sms():

            """Send a dynamic reply to an incoming text message"""

            # Start our TwiML response
            resp = twilio.twiml.Response()
            # Get the message the user sent our Twilio number
            body = request.form['Body']
            from_number = request.values.get('From')

            # Determine the right reply for this message

            if body == 'Mansplain it to me!':

                #open file scavengerList and add new number to file
                nameHandle = open('scavengerlist.txt', 'a')
                nameHandle.write(from_number)
                nameHandle.write('\n')
                nameHandle.close()

                #text reply to new participant with welcome and first clue of hunt
                resp.message("Hi, what would you like mansplained to you? You can text our man experts a word or phrase or a photo of what you would like mansplained.")
                resp.message("Text WORD to send a word or phrase or PHOTO to text a photo.")

            elif body == "TEXT":

                resp.message("Thanks for the text, sweetheart. Let me go get a man to explain that to you.")

                #CODE TO RETURN WIKI RESULTS

            elif body == "PHOTO":

                myURL = request.form['MediaUrl0']

                imageurl = api.tag_image_urls(myURL)

                tag = imageurl["results"][0]["result"]["tag"]["classes"][1]


                if __name__ == "__main__":
                    app.run(debug=True)

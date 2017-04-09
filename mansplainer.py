#!/usr/bin/python

from clarifai.rest import ClarifaiApp
import searchWikipedia as wiki

#Clarifai keys
#os.environ["CLARIFAI_APP_ID"]="T6ZF_EuGDplxDhLUk2qtkCvEJdn_lT_usf00zAWc"
#os.environ["CLARIFAI_APP_SECRET"]="clwcHLrrami5VJj2PzIGSc7tiwFUGbTsP8Fg0HDd"
appC = ClarifaiApp("T6ZF_EuGDplxDhLUk2qtkCvEJdn_lT_usf00zAWc", "clwcHLrrami5VJj2PzIGSc7tiwFUGbTsP8Fg0HDd")  # assumes environment variables are set.
#model = app.models.get("general-v1.3")

from flask import Flask, request, redirect
from twilio.rest import Client
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
import requests

account_sid = "ACbe0730baeb75b5f6a870f65bfabe386d"
auth_token = "0d08cdad7424c231bc1f34a6b3456777"
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/incoming_sms", methods=['GET', 'POST'])

def incoming_sms():

    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number

    body = request.form['Body']
    from_number = request.form['From']

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    body = body.upper()

    if body == 'MANSPLAIN':

        resp.message("Hi there sweetheart, what would you like mansplained to you today? You can text our man experts a nice photo and they can help you understand what it's about.")
        return str(resp)

    else:

        myURL = request.form["MediaUrl0"]
        req = requests.get(myURL)
        image_URL = req.url

        model = appC.models.get("general-v1.3")

        imageresult = model.predict_by_url(url=image_URL)

        tag = imageresult["outputs"][0]["data"]["concepts"][0]["name"]
        tag2 = imageresult["outputs"][0]["data"]["concepts"][1]["name"]

        mansplanation = wiki.getSummaryFromWiki(tag)

        if mansplanation == None:
            mansplanation = wiki.getSummaryFromWiki(tag2)

        resp.message("Okay, I can understand how a girl like you might find that confusing. Let me mansplain that for you: \n\n {} \n\nI hope that was helpful, but you still look a little lost. How about we discuss this further over a nice dinner? Don't worry, I have your number now, so I'll call you.".format(str(mansplanation)))

        #resp.message("I hope that was helpful, but you still look a little lost. How about we discuss this further over a nice dinner? Don't worry, I have your number now, so I'll call you.")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

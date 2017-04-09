#!/usr/bin/python
from clarifai.rest import ClarifaiApp
import searchWikipedia as wiki
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse
import requests
import random

MAN_TALKS = ["111Hi there sweetheart, what would you like mansplained to you today? You can send our man experts a nice photo and they can help you understand what it's about.",
                "222Hello honey, what would you like mansplained to you today? Send a nice photo to our man experts, they will help you understand what it's about.",
                "333Hello dear, how are you doing, what would you like mansplained to you today? You can text our man experts a nice photo and they can help you understand what it's about."]

MAN_EXPLAIN = ["111Okay, I can understand this is challenging for you. Let me mansplain that for you: \n\n {} \n\nI hope that was helpful, if not we could discuss this further over a nice dinner. Don't worry, I have your number now, so I'll call you.",
                "222Wow, nice photo. Let me mansplain that for you: \n\n {} \n\nI hope that was helpful, but you still look a little lost. How about we discuss this further over a nice dinner? Don't worry, I have your number now, so I'll call you.",
                "333Okay, I can understand how a girl like you might find that confusing. Let me mansplain that for you: \n\n {} \n\nI hope that was helpful, but you still look a little lost. How about we discuss this further over a nice dinner? Don't worry, I have your number now, so I'll call you."]

appC = ClarifaiApp("T6ZF_EuGDplxDhLUk2qtkCvEJdn_lT_usf00zAWc", "clwcHLrrami5VJj2PzIGSc7tiwFUGbTsP8Fg0HDd")
account_sid = "ACbe0730baeb75b5f6a870f65bfabe386d"
auth_token = "0d08cdad7424c231bc1f34a6b3456777"
client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/incoming_sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    try:
        myURL = request.form["MediaUrl0"]
    except Exception as e:
        myURL = 'NaN'

    if myURL != 'NaN':
        myURL = request.form["MediaUrl0"]
        req = requests.get(myURL)
        image_URL = req.url
        model = appC.models.get("general-v1.3")
        imageresult = model.predict_by_url(url=image_URL)

        mansplanation = None
        for tag in imageresult["outputs"][0]["data"]["concepts"]:
            mansplanation = wiki.getSummaryFromWiki(tag["name"])
            if mansplanation != None:
                break

        reply_num = random.randint(0,2)
        resp.message(MAN_EXPLAIN[reply_num].format(str(mansplanation)))
        return str(resp)
    else:
        reply_num = random.randint(0,2)
        resp.message(MAN_TALKS[reply_num])
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

#!/usr/bin/python

import os
from clarifai.client import ClarifaiApi

#Clarifai keys
os.environ["CLARIFAI_APP_ID"]="T6ZF_EuGDplxDhLUk2qtkCvEJdn_lT_usf00zAWc"
os.environ["CLARIFAI_APP_SECRET"]="clwcHLrrami5VJj2PzIGSc7tiwFUGbTsP8Fg0HDd"
api = ClarifaiApi()  # assumes environment variables are set.

from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient as twr

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

    if body == 'Join scavenger hunt':

        #open file scavengerList and add new number to file
        nameHandle = open('scavengerlist.txt', 'a')
        nameHandle.write(from_number)
        nameHandle.write('\n')
        nameHandle.close()

        #text reply to new participant with welcome and first clue of hunt
        resp.message("Hi, welcome to HackNY Scavenger Hunt! The first clue is clock. You must text a photo of a clock that our AI tags and recognizes as a clock to get the next clue. Good Luck!")

    else:
        myURL = request.form['MediaUrl0']

        imageurl = api.tag_image_urls(myURL)

        tag_collection = []
        numTags = 10
        for i in range(0, numTags):
            tag = imageurl["results"][0]["result"]["tag"]["classes"][i]
            #add tag to collection list
            tag_collection.append(tag)

        counter = 0
        for x in tag_collection:

            winner = get_winner()

            #AI tag returned correct tag, found first clue
            if x == "clock":
                #send text with next clue
                resp.message("Good work, hacker! The next clue is chair.")
                break
            #AI tag returned correct tag, found second clue
            elif x == "chair":
                #send text with next clue
                resp.message("You're doing great! The next clue is bottle.")
                break
            #AI tag returned correct tag, found last clue
            elif x == "bottle":
                #user found all clues, but all winner slots taken
                if winner <= 0:
                    #notify user by text
                    resp.message("You finished the HackyNY Scavenger Hunt, but you didn't finish in time to win. Hope you had fun playing!")
                    break
                else:
                    #first place
                    if winner == 3:
                        winnerList.append(from_number)
                        resp.message("You are the winner, congratulations!") #notify winner by text
                    #second place
                    elif winner == 2:
                        winnerList.append(from_number)
                        resp.message("You won second place! Awesome!") #notify winner by text
                    elif winner == 1:
                        winnerList.append(from_number)
                        resp.message("You won third place! You are so amazing!") #notify winner by text
                    #found winner, so decrement number of available winner slots by 1
                    winner -= 1
            else:
                counter += 1
                if counter == 10:
                    resp.message("Your photo didn't return the right tag, sorry!")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

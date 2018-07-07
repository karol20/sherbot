import os, sys
from flask import Flask, request
from pymessenger import Bot
import requests
import pprint
import json
import buttons
import parserek


Page_Access_Token = "EAADGZCGstHcwBAJq6BUSMZAZBfORzfrhu0k9kHtFvUTVPZBRhMnQd1vlpm94vBGwo8tNlZCSKh18ScPR5H18i8JUJntvvS6rKirJOmIag9LSxPOW9R9BQgu39vlC0MMkmMTBcPLxnXUJGQu6SVlf2ikCaH13opzQKiTizA5aWJwZDZD"
Webhook_Token = "WHVT"
bot = Bot(Page_Access_Token)
url = 'https://graph.facebook.com/v2.6/me/messenger_profile?access_token=%s' %(Page_Access_Token)
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def ChatBot():


    if request.method == 'GET':
        if request.args.get("hub.verify_token") == Webhook_Token:

            return request.args["hub.challenge"], 200
        else:
            return "nie poprawny token weryfikacyjny", 403

    else:


        kwlist = request.get_json()

        for entry in kwlist['entry']:


            for messaging in entry['messaging']:

                # id nadawcy
                nadawca = messaging['sender']['id']

                if 'postback' in messaging:
                    #początek rozmowy / przycisk rozpocznij/ nawiązanie połączenia z akinatorem
                    if messaging['postback']['payload'] == "Rozpocznij":
                        #
                        global page
                        page = parserek.sesion()
                        buttons.button(nadawca, bot)
                        print("rozpocznij")
                    #postaback po nacisnięciu zaczynajmy
                    elif messaging['postback']['payload'] == "start":
                        global pierwsze
                        pierwsze = True
                        pytanie = parserek.get_pytanie(page)
                        buttons.odp(nadawca, pytanie, bot)
                        print("zaczynajmy")
                    elif messaging['postback']['payload'] == "zgadza się":
                        bot.send_text_message(nadawca, "zgadza się")
                    elif messaging['postback']['payload'] == "Nie zgadza się":
                        bot.send_text_message(nadawca, "nie zgadza się")

                elif 'quick_reply' in messaging['message']:
                        parserek.wiadomosc(nadawca,messaging,page,bot)



        return "ok", 200


if __name__ == '__main__':
    app.run(debug=True, port = 5000)
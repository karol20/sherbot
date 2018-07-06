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
                    #postaback po nacisnięciu zaczynajmy
                    else:
                        global pierwsze
                        pierwsze = True
                        pytanie = parserek.pytanie(page)
                        buttons.odp(nadawca, pytanie, bot)

                elif 'quick_reply' in messaging['message']:

                    try:
                        propozycja = parserek.check_win(page)
                        #buttons.win_buttons(nadawca, propozycja, bot)
                        parserek.kill(page)

                    except Exception:
                        if pierwsze:
                            wyb = messaging['message']['quick_reply']['payload']
                            dr = parserek.answer(page, wyb)



                        else:
                            wyb = messaging['message']['quick_reply']['payload']
                            pytanie = parserek.pytanie(page)
                            buttons.odp(nadawca,pytanie, bot)
                            dr = parserek.answer(page,wyb)

                        pierwsze = False



        return "ok", 200


if __name__ == '__main__':
    app.run(debug=True, port = 5000)
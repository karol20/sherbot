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
                    if messaging['postback']['payload'] == "Rozpocznij" or messaging['postback']['payload'] == "again":
                        global page
                        page = parserek.sesion()
                        if messaging['postback']['payload'] == "Rozpocznij":
                            buttons.button(nadawca, bot)
                        elif messaging['postback']['payload'] == "again":
                            pytanie = parserek.get_pytanie(page)
                            buttons.odp(nadawca, pytanie, bot)
                        print("rozpocznij")
                    #postaback po nacisnięciu zaczynajmy
                    elif messaging['postback']['payload'] == "start":
                        pytanie = parserek.get_pytanie(page)
                        buttons.odp(nadawca, pytanie, bot)
                        print("zaczynajmy")

                    elif messaging['postback']['payload'] == "zgadza się":
                        buttons.zgadza(nadawca, bot)
                        parserek.kill(page)

                    elif messaging['postback']['payload'] == "Nie zgadza się":
                        buttons.nie_zgadza(nadawca,bot)
                    elif messaging['postback']['payload'] == "dalej":
                        bot.send_text_message(nadawca, "dalej")

                    # elif messaging['postback']['payload'] == "again":
                    #     global page
                    #     bot.send_text_message(nadawca, "again")
                    #     page = parserek.sesion()
                    #     buttons.button(nadawca, bot)

                elif 'quick_reply' in messaging['message']:
                        parserek.wiadomosc(nadawca,messaging,page,bot)



        return "ok", 200


if __name__ == '__main__':
    app.run(debug=True, port = 5000)
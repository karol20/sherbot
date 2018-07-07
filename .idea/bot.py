import os, sys
from flask import Flask, request
from pymessenger import Bot
import requests
import json
import buttons
import parserek


Page_Access_Token = ""
Webhook_Token = ""
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
                        global page
                        page = parserek.sesion()
                        buttons.button(nadawca, bot)
                    #nawiązanie kolejnego połączenia w tej samej sesji
                    elif messaging['postback']['payload'] == "again":
                        page = parserek.sesion()
                        pytanie = parserek.get_pytanie(page)
                        buttons.odp(nadawca, pytanie, bot)
                    #postaback po nacisnięciu zaczynajmy
                    elif messaging['postback']['payload'] == "start":
                        pytanie = parserek.get_pytanie(page)
                        buttons.odp(nadawca, pytanie, bot)
                        print("zaczynajmy")
                    #odgadnięta odpowiedź
                    elif messaging['postback']['payload'] == "zgadza się":
                        buttons.zgadza(nadawca, bot)
                    #błędna odpowiedź
                    elif messaging['postback']['payload'] == "Nie zgadza się":
                        buttons.nie_zgadza(nadawca,bot)
                    #kontynuowanie gry po błędnej odpowiedzi
                    elif messaging['postback']['payload'] == "dalej":
                        parserek.kont(page)
                        pytanie = parserek.get_pytanie(page)
                        buttons.odp(nadawca, pytanie, bot)

                #zadanie pytania/przyjęcie odpowiedzi/sprawdzenie czy akinator znalazł osobę
                elif 'quick_reply' in messaging['message']:
                        parserek.wiadomosc(nadawca,messaging,page,bot)



        return "ok", 200


if __name__ == '__main__':
    app.run(debug=True, port = 5000)
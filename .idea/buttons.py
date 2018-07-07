from pymessenger import Bot

def button(nadawca, bot):

    button = {
        "recipient": {
            "id": nadawca
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Witaj, jestem Sherbot. Pomyśl o dowolnej postaci, a ja wydedukuję kto to.",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Zaczynajmy",
                            "payload": "start"
                        }
                    ]
                }
            }
        }
    }
    bot.send_raw(button)



def odp(nadawca, pytanie, bot):
    WWW = {
        "recipient": {
            "id": nadawca
        },
        "message": {
            "text": pytanie,
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Tak",
                    "payload": "0"
                },
                {
                    "content_type": "text",
                    "title": "Nie",
                    "payload": "1"
                },
                {
                    "content_type": "text",
                    "title": "Nie wiem",
                    "payload": "2"
                },
                {
                    "content_type": "text",
                    "title": "Chyba tak",
                    "payload": "3"
                },
                {
                    "content_type": "text",
                    "title": "Chyba nie",
                    "payload": "4"
                },
            ]
        }
    }
    bot.send_raw(WWW)




def reply(nadawca, propozycja, bot):
    rep = {
        "recipient": {
            "id": nadawca
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": propozycja,
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Zgadza się",
                            "payload": "zgadza się"
                        },
                        {
                            "type": "postback",
                            "title": "Nie zgadza się",
                            "payload": "Nie zgadza się"
                        }

                    ]
                }
            }
        }
    }
    bot.send_raw(rep)



def zgadza(nadawca, bot):

    zgadza= {
        "recipient": {
            "id": nadawca
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Hah, elementary my dear watson.",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Zagraj ponownie",
                            "payload": "again"
                        }
                    ]
                }
            }
        }
    }
    bot.send_raw(zgadza)

def nie_zgadza(nadawca, bot):

    nZgadza = {
        "recipient": {
            "id": nadawca
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Hmm, najwyraźniej nie miałem odpowiedniej ilości danych.",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Zagraj ponownie",
                            "payload": "again"
                        },
                        {
                            "type": "postback",
                            "title": "graj dalej",
                            "payload": "dalej"
                        }

                    ]
                }
            }
        }
    }
    bot.send_raw(nZgadza)
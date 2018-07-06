from pymessenger import Bot

def menu():
    menu ={
        "persistent_menu": [
            {
                "locale": "default",
                "composer_input_disabled": "true",
                "call_to_actions": [
                    {
                        "title": "Strona Bota",
                        "type": "web_url",
                        "url": "https://www.facebook.com/Chat.Bot2000/"
                    },
                    {
                        "title": "Akiantor",
                        "type": "web_url",
                        "url": "https://akinator.com"
                    }
                ]
            }
        ]
    }
    return menu


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
                    "text": "Witaj, jestem Sherlock bot. Pomyśl o dowolnej postaci, a ja odgadne kto to.",
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

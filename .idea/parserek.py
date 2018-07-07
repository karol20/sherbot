from lxml import html
import requests
import urllib3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import buttons
from pymessenger import Bot
import buttons
def sesion():
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\Acer\Desktop\robota\geckodriver.exe')
    driver.get("https://pl.akinator.com/game")
    driver.back()
    return driver
def get_pytanie(driver):

    q = driver.find_element_by_class_name("question-text").text
    return q

def check_win(driver):

        p = guess = driver.find_element_by_class_name("proposal-title").text
        return p

def get_guess(driver):
    guess = driver.find_element_by_class_name("proposal-title")
    return guess
def answer(driver,wyb):
    d={
        "0":"""//*[@id="a_yes"]""",
        "1":"""//*[@id="a_no"]""",
        "2":"""//*[@id="a_dont_know"]""",
        "3":"""//*[@id="a_probably"]""",
        "4":"""//*[@id="a_probaly_not"]""",
    }
    dr = driver.find_element_by_xpath(d[wyb]).click()
    return dr


def kill(driver):
    driver.close()
def wiadomosc(nadawca,messaging,driver,bot):


    # try:
    #     driver.find_element_by_xpath("""//*[@id="game_content"]/div/div[3]/div[1]/div[1]/p""")
    #     print("______________")
    # except:
        # try:
        #
        #     propozycja = check_win(driver)
        #     print(propozycja)
        #
        #     buttons.reply(nadawca, propozycja, bot)
        #     print("quick rep try")
        #     # parserek.kill(page)
        #
        # except Exception:
        try:
            driver.find_element_by_class_name("proposal-title")
            # propozycja = check_win(driver)
            # print(propozycja)
            # buttons.reply(nadawca, propozycja, bot)
            # print("quick rep try")
        except:

            wyb = messaging['message']['quick_reply']['payload']
            dr = answer(driver, wyb)
            pytanie = get_pytanie(driver)
            buttons.odp(nadawca, pytanie, bot)
            print("exept if true")
        else:
            #print(driver.page_source)
            propozycja = check_win(driver)
            wiadomosc = "Myślisz o %s" %(propozycja)
            buttons.reply(nadawca, wiadomosc, bot)
            print("quick rep try")

def kont(page):
    pass
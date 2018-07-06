from bs4 import BeautifulSoup
from lxml import html
import requests
import mechanicalsoup
import urllib3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import buttons

def sesion():
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Firefox(firefox_options=options, executable_path=r'C:\Users\Acer\Desktop\robota\geckodriver.exe')
    driver.get("https://pl.akinator.com/game")
    driver.back()

    return driver

def pytanie(driver):

    q = driver.find_element_by_xpath("""//*[@id="game_content"]/div/div[3]/div[1]/div[2]/p""").text
    return q

def check_win(driver):
    p = driver.find_element_by_xpath("""//*[@id="game_content"]/div/div[3]/div[1]/div[2]/p/span[1]""").text
    return p

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



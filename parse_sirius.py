import time

import requests
from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.by import By

from db import Database

db = Database('data.db')


def get_data():
    result = []

    url = 'https://siriuscollege.ru/090207-informatsionnie-sistemi-i-programmirovanie'

    driver = webdriver.Chrome('C:\\Users\\hdhrh\\PycharmProjects\\CheckMyAdvertBot\\webdriver\\chromedriver.exe')

    try:
        driver.get(url=url)
        time.sleep(3)

        trs = driver.find_elements(By.TAG_NAME, 'tr')

        for tr in trs[1:]:
            snils = tr.find_elements(By.TAG_NAME, 'td')[1].text

            result.append(
                {
                    'count': tr.find_elements(By.TAG_NAME, 'td')[0].text,
                    'snils': snils,
                    'balls': tr.find_elements(By.TAG_NAME, 'td')[-3].text
                }
            )

        for dct in result:
            if not db.check_number(dct['count']):
                db.set_count(dct['count'])
                db.set_snils(dct['count'], dct['snils'])
                db.set_balls(dct['count'], dct['balls'])

            else:
                pass

        return result

    except Exception as e:
        if Exception is IndexError:
            time.sleep(6)
            return get_data()
    finally:
        driver.close()


def most_main_check():
    if db.most_main_check():
        return True
    else:
        return False


def main():
    get_data()
    most_main_check()


if __name__ == '__main__':
    main()

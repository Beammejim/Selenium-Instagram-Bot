from config import user, pwd, comments, speed, hashtag
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from random import *
import time


class InstaAutomate():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)

    def __init__(self):
        self.login()
        self.find_hashtag()
        self.navitab()
        self.like_comment()

    def login(self):
        self.driver.get('https://instagram.com')
        time.sleep(3)
        self.driver.find_element_by_xpath('//input[@name="username"]')\
            .send_keys(user)
        self.driver.find_element_by_xpath('//input[@name="password"]')\
            .send_keys(pwd)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')\
            .click()
        time.sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
            .click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()

    def find_hashtag(self):
        self.driver.find_element_by_xpath('/html//div[@id="react-root"]/section/nav//input')\
            .send_keys('#' + hashtag)
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')\
            .click()
        time.sleep(5)

    def navitab(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div') \
            .click()

    def pagkdku(self):
        self.actions.key_down(Keys.RIGHT).key_up(Keys.RIGHT).perform()

    def like_comment(self):
        while True:
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')\
                        .click()
                print('like!')
                time.sleep(1)
            except NoSuchElementException:
                print('like not found')
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')\
                    .click()
                time.sleep(1)
                self.driver.find_element_by_xpath('//textarea[@placeholder="Kommentar hinzufügen ..."]')\
                    .send_keys(comments[randint(0, 8)])
                time.sleep(1)
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button')\
                    .click()
                print('post comment')
                time.sleep(1)
            except NoSuchElementException:
                print('Comment not found')
            try:
                self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button')\
                        .click()
                print('follow')
                time.sleep(1)
            except NoSuchElementException:
                print('follow not found')
            time.sleep(speed)
            self.pagkdku()


def main():
    InstaAutomate()


if __name__ == '__main__':
    main()


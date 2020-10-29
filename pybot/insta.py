from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self,userName,password):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Akceptuję')]")\
            .click()
        sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(userName)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Nie teraz')]")\
            .click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Nie teraz')]")\
            .click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Obserwuj')]")\
            .click()
        sleep(20)




InstaBot('DodzioBot69','DodzioBot69@')
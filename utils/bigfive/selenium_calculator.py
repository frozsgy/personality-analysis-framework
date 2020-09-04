from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re


class TestParse():
    def __init__(self):

        binary = FirefoxBinary('/usr/lib/firefox/firefox')
        self.driver = webdriver.Firefox(executable_path='geckodriver', firefox_binary=binary)

        self.driver.implicitly_wait(10)
        self.base_url = "https://www.truity.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def parse(self, args):
        #print ("qsad")
        driver = self.driver

        driver.get(self.base_url + "/view/tests/big-five-personality")

        driver.find_element(By.XPATH, "//a[text()='Take it!']").click()

        element = driver.find_element_by_id("edit-submitted-a1-" + str(args[0]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c1-" + str(args[1]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e1-" + str(args[2]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n1-" + str(args[3]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o1-" + str(args[4]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-a2-" + str(args[5]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c2-" + str(args[6]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e2-" + str(args[7]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n2-" + str(args[8]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o2-" + str(args[9]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-a3-" + str(args[10]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c3-" + str(args[11]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e3-" + str(args[12]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n3-" + str(args[13]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o3-" + str(args[14]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-a4-" + str(args[15]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c4-" + str(args[16]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e4-" + str(args[17]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n4-" + str(args[18]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o4-" + str(args[19]))
        driver.execute_script("arguments[0].click();", element)

        driver.find_element_by_css_selector(
            "#webform-client-form-17315 > div > div.form-actions > button[name=\"op\"]").click()

        element = driver.find_element_by_id("edit-submitted-a5-" + str(args[20]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c5-" + str(args[21]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e5-" + str(args[22]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n5-" + str(args[23]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o5-" + str(args[24]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-a6-" + str(args[25]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c6-" + str(args[26]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e6-" + str(args[27]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n6-" + str(args[28]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o6-" + str(args[29]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-a7-" + str(args[30]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c7-" + str(args[31]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e7-" + str(args[32]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n7-" + str(args[33]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o7-" + str(args[34]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-a8-" + str(args[35]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c8-" + str(args[36]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e8-" + str(args[37]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n8-" + str(args[38]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-o8-" + str(args[39]))
        driver.execute_script("arguments[0].click();", element)

        driver.find_element_by_xpath("(//button[@name='op'])[3]").click()

        element = driver.find_element_by_id("edit-submitted-o-word-1-" + str(args[40]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c-word-1-" + str(args[41]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e-word-1-" + str(args[42]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-a-word-1-" + str(args[43]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n-word-1-" + str(args[44]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-o-word-2-" + str(args[45]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c-word-2-" + str(args[46]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e-word-2-" + str(args[47]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-a-word-2-" + str(args[48]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n-word-2-" + str(args[49]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-o-word-3-" + str(args[50]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c-word-3-" + str(args[51]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e-word-3-" + str(args[52]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-a-word-3-" + str(args[53]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n-word-3-" + str(args[54]))
        driver.execute_script("arguments[0].click();", element)

        element = driver.find_element_by_id("edit-submitted-o-word-4-" + str(args[55]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-c-word-4-" + str(args[56]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-e-word-4-" + str(args[57]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-a-word-4-" + str(args[58]))
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_id("edit-submitted-n-word-4-" + str(args[59]))
        driver.execute_script("arguments[0].click();", element)

        driver.find_element_by_xpath("(//button[@name='op'])[3]").click()
        driver.find_element_by_xpath("(//button[@name='op'])[3]").click()

        result = self.getBigFiveScore(driver.page_source)

        driver.quit()

        return result

    def getValueOfLabel(self, text, label):
        labelIndex = text.find('"name":"' + label + '"')
        valueIndex = text.find("value", labelIndex) + 7
        value = ""
        while True:
            if text[valueIndex] >= '0' and text[valueIndex] <= "9":
                value += text[valueIndex]
            else:
                break
            valueIndex += 1
        return int(value)

    def getBigFiveScore(self, text):
        #dict = {"Openness" : "", "Conscientiousness" : "", "Extraversion" : "", "Agreeableness" : "", "Neuroticism" : ""}
        dict = {"Agreeableness": "", "Conscientiousness": "",
                "Extraversion": "",  "Neuroticism": "", "Openness": ""}
        for eachKey in dict:
            dict[eachKey] = self.getValueOfLabel(text, eachKey[0])
        return dict

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)




ppl = {"name": "scores"}
       
for key, value in ppl.items():
    cp = TestParse()
    questionnarie = list(map(int, value.split()))
    questionnarie = [i + 1 for i in questionnarie]
    
    print(key)
    print(cp.parse(questionnarie))
    print("-"*40)

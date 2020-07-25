from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
downloadDir = os.getcwd()
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", downloadDir)
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/html")
driver = webdriver.Firefox(firefox_profile=fp)
driver.get("https://sketch2code.azurewebsites.net/")
sleep(2)
driver.find_element_by_id("imageData").send_keys("/home/janukan/Pictures/5_11.png")
sleep(6)
driver.find_element_by_class_name("finish-img").click()

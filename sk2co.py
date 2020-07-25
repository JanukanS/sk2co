import click
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import os
from time import sleep

def SetUpDriver(downloadDir):
    fp = webdriver.FirefoxProfile()
    options = Options()
    options.add_argument("--headless")
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", downloadDir)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/html")
    return webdriver.Firefox(firefox_profile=fp,firefox_options=options)

@click.command()
@click.argument('image')
def process(image):
    currentDir = "".join([os.getcwd(),"/"])
    driver = SetUpDriver(currentDir)
    driver.get("https://sketch2code.azurewebsites.net/")
    sleep(1)
    driver.find_element_by_id("imageData").send_keys("".join([currentDir,image]))
    sleep(6)
    driver.find_element_by_class_name("finish-img").click()
    driver.quit()

if __name__ == "__main__":
    process()

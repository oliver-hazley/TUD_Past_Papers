import os
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from dir_path import CHROMEDRIVER_DIRECTORY, DOWNLOAD_DIRECTORY

# ###############   PLEASE NO JUDGE, THIS IS NOT ELEGANT, BUT IT DOES THE JOB


# Configure Chrome to allow download of pdfs without opening seperate window

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": DOWNLOAD_DIRECTORY, # Change default directory for downloads
"download.prompt_for_download": False, # To auto download the file
"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True # It will not show PDF directly in chrome
})

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_DIRECTORY, options=options)

# You need to create a config txt file in the same directory in the following format:
# myStudentID
# myPassword

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]



class PastPapers:

    def __init__(self, username, password):
        self.username = username
        self.password = password


    def login(self):
        driver.get('https://library.it-tallaght.ie/er.html')
        sleep(2) # Allow page to load
        login_link = driver.find_element_by_xpath("//div[@class='badge.red']/a")
        login_link.click()
        sleep(2) # Allow page to load 

        user_name_elem = driver.find_element_by_id('username')
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        passworword_elem = driver.find_element_by_id('password')
        passworword_elem.clear()
        passworword_elem.send_keys(self.password)
        passworword_elem.send_keys(Keys.ENTER)
        sleep(2) # Allow page to load

    def getPapers(self):
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div/div[1]/ul/li[4]/a").click()
        driver.find_element_by_xpath("/html/body/form[1]/button").click()
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/ul/li[3]/span[1]").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div/ul/li[16]/span[2]").click()
        sleep(2)


        for i in range(9955, 10018):
            try:
                driver.find_element_by_xpath(f"//li[@data-nodeid='{i}']/span[contains(@class,'expand-icon')]").click()
            except:
                pass

            try:
                driver.find_element_by_xpath(f"//li[@data-nodeid='{i}']/a").click()
            except:
                pass

    def closeBrowser(self):
        sleep(5) # to allow time for downloads to finish, if your wifi is slow just increase the number
        driver.close()




def __main__():
    bot = PastPapers(username, password)
    bot.login()
    bot.getPapers()
    bot.closeBrowser()

if __name__ == "__main__":
    __main__()



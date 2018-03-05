from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import unittest

#Browser path
geckodriver_path = r"C:\Anaconda2\misc\geckodriver-v0.19.1-win64\geckodriver.exe"
headless_chrome = r"C:\Anaconda2\misc\chrome_headless\chromedriver.exe"
browser_options = Options()
browser_options.add_argument('--headless')
browser_options.add_argument('--disable-gpu')

using_firefox = True  # if false user uses chrome
using_headless = True # if true, browser won't open up

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
    #user opens browser
        #firefox
        if (using_firefox):
            if using_headless:
                self.browser = webdriver.Firefox(firefox_options=browser_options, executable_path=geckodriver_path)
            else:
                self.browser = webdriver.Firefox(executable_path=geckodriver_path)
        #chrome
        else:
            browser_options.binary_location = r"C:\Users\Irene Herero\AppData\Local\Google\Chrome SxS\Application\chrome.exe"
           
            if using_headless:
                self.browser = webdriver.Chrome(chrome_options=browser_options, executable_path=headless_chrome)
            else:
                self.browser = webdriver.Chrome(executable_path=headless_chrome)
    
    def tearDown(self):
            self.browser.close()

    #start teststory
    def test_can_start_a_list_and_retrieve_it_later(self):
        
        #user heard about the new online to-do application and opens the website
        self.browser.get('http://localhost:8000')

        #when the page loaded the user knows he/she is on the right page because the page title says so
        self.assertIn("To-Do", self.browser.title, "Browse title was " + self.browser.title)
        self.fail('Finish the test!') #always fails, remainder to finish the test

        #the user can type in a to-do item right away

        #the user types "make a 3D model car" in a text box

        #when hitting enter, the page updates and now lists "1. make a 3D model car"

        #the textbox to add new items is still there
        #the user enters "make car texture"

        #the page updates again and now lists both items

        #the user doesn't want other users to be able to see or edit his/her own list. 
        #This is why the site generates a unique url for every user. There is a little explanatory text to that effect 

        #when the user visits his/her personal url, the user will see his own list and can edit it

        #after checking andupdating the website, the user closes the browser

if __name__ == "__main__":
    unittest.main()
    




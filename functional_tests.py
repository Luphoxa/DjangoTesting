from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import unittest
import time

# Browser path
geckodriver_path = r"C:\Anaconda2\misc\geckodriver-v0.19.1-win64\geckodriver.exe"
headless_chrome = r"C:\Anaconda2\misc\chrome_headless\chromedriver.exe"
browser_options = Options()
browser_options.add_argument('--headless')
browser_options.add_argument('--disable-gpu')

using_firefox = True  # if false user uses chrome
using_headless = True  # if true, browser won't open up


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        # user opens browser
        # firefox
        if (using_firefox):
            if using_headless:
                self.browser = webdriver.Firefox(firefox_options=browser_options, executable_path=geckodriver_path)
            else:
                self.browser = webdriver.Firefox(executable_path=geckodriver_path)
        # chrome
        else:
            browser_options.binary_location = r"C:\Users\Irene Herero\AppData\Local\Google\Chrome SxS\Application\chrome.exe"

            if using_headless:
                self.browser = webdriver.Chrome(chrome_options=browser_options, executable_path=headless_chrome)
            else:
                self.browser = webdriver.Chrome(executable_path=headless_chrome)

    def tearDown(self):
        self.browser.close()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    # start teststory
    def test_can_start_a_list_and_retrieve_it_later(self):

        # user heard about the new online to-do application and opens the website
        self.browser.get('http://localhost:8000')

        # when the page loaded the user knows he/she is on the right page because the page title says so
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # the user can type in a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # the user types "make a 3D model car" in a text box
        inputbox.send_keys('Make a 3D Model Car')

        # when hitting enter, the page updates
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)  # gives the page time to load

        # the page now lists "1. Make a 3D Model Car"
        self.check_for_row_in_list_table('1: Make a 3D Model Car')

        # the textbox to add new items is still there
        # the user enters "Make car texture"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Make car texture')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the page updates again and now lists both items
        self.check_for_row_in_list_table('1: Make a 3D Model Car')
        self.check_for_row_in_list_table('2: Make car texture')

        # the user doesn't want other users to be able to see or edit his/her own list.
        # This is why the site generates a unique url for every user. There is a little explanatory text to that effect
        self.fail('Finish the test!') # always fails, remainder to finish the test
        # when the user visits his/her personal url, the user will see his own list and can edit it

        # after checking andupdating the website, the user closes the browser


if __name__ == "__main__":
    unittest.main()

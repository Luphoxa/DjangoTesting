from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#Browser paths
geckodriver_path = r"C:\Anaconda2\misc\geckodriver-v0.19.1-win64\geckodriver.exe"
#headless_chrome = r"C:\Anaconda2\misc\chrome_headless\chromedriver.exe"

#setting up headless chrome
#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.binary_location = r"C:\Users\Irene Herero\AppData\Local\Google\Chrome SxS\Application\chrome.exe"

#open chrome
#driver = webdriver.Chrome(executable_path=headless_chrome, chrome_options=chrome_options)

#open firefox
driver = webdriver.Firefox(executable_path=geckodriver_path)

#start test
driver.get('http://localhost:8000')
assert "Django" in driver.title
#print "Test successful"

#driver.close()




import unittest

from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')


class WebTest(unittest.TestCase):
    def testPollsHomePage(self):
        driver.get('http://localhost:8000/polls/')
        element = driver.find_element_by_css_selector('body > h4')
        self.assertEquals(element.text, 'List questions')
        driver.quit()

if __name__ == '__main__':
    unittest.main()

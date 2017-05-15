import unittest

from selenium import webdriver

class WebTest(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def testPollsHomePage(self):
        self.driver.get('http://localhost:8000/polls/')
        element = self.driver.find_element_by_css_selector('body > h4')
        self.assertEquals(element.text, 'List questions')

    def testPollsHomePage(self):
        self.driver.get('http://localhost:8000/polls/')
        element = self.driver.find_element_by_css_selector('body > h4')
        self.assertEquals(element.text, 'List questions')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

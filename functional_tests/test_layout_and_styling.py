from .base import FunctionalTest
from django.test import tag
from selenium.webdriver.common.keys import Keys

from .list_page import ListPage

class LayoutAndStylingTest(FunctionalTest):
    @tag('pi2-incompatible')
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        list_page= ListPage(self)
        inputbox = list_page.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)

        list_page.wait_for_row_in_list_table('testing', 1)
        inputbox = list_page.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            575,
            delta=100
        )

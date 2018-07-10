from .base import FunctionalTest
from django.test import tag
from selenium.webdriver.common.keys import Keys

class LayoutAndStylingTest(FunctionalTest):
    @tag('pi2-incompatible')
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10
        )

    def test_layout_and_styling_part_2(self):
        # Edith goes to the home page
        self.browser.get(self.live_server_url)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.get_item_input_box()
        # NOTE(steve): for this test to work properly as the 
        # book intended, use 512 not 640. 640 is for the pi2
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            640,
            delta=10
        )

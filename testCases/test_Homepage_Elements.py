import pytest
from selenium.webdriver.common.by import By
from pageObjects.homepage import Homepage
from testCases.conftest import *
from utilities.utils_functions import GenerateLog


class Test_WebElement:
    """
       This test class tests the functionality of various elements on the DEMOQA homepage.

       It includes tests for:
       - Page loading to ensure the correct title is displayed.
       - Presence of header image.
       - Clickability of the header image link.
       - Presence of footer text.
       - Number of categories displayed on the homepage.
       - Clickability of various categories like elements, forms, alerts and windows, widgets, interactions, and books app.
       """

    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.logger = GenerateLog.generate_log()

    def test_page_loading(self):
        self.logger.info("Title of HomePage: PASSED")
        assert self.driver.title == "DEMOQA"

    def test_logo_presence(self):
        self.header = self.homepage.get_header_element()
        self.logger.info("Header Logo Presence: PASSED")
        self.driver.save_screenshot(f".//Screenshots/{Test_WebElement.test_logo_presence.__name__}.png")
        assert bool(self.header.find_element(By.TAG_NAME, "img"))

    def test_logo_clickable(self):
        header = self.homepage.get_header_element()
        header.find_element(By.TAG_NAME, 'a').click()
        self.logger.info("Logo is clickable: PASSED")
        assert self.driver.current_url == base_url
        assert self.driver.title == "DEMOQA"

    def test_footer_presence(self):
        footer = self.homepage.get_footer()
        self.logger.info("Footer presence: PASSED")
        assert bool(footer)
        assert footer.text == self.homepage.footer_text

    def test_nums_of_category(self):
        category_size, name_list = self.homepage.get_nums_of_category_and_names()
        self.logger.info("Categories Presence and size: PASSED")
        assert category_size == 6
        assert "Widgets" in name_list

    def test_elements_cat_click(self):
        self.homepage.click_elements()
        self.logger.info("Elements Category Presence: PASSED")
        assert 'elements' in self.driver.current_url

    def test_forms_cat_click(self):
        self.homepage.click_forms()
        self.logger.info("Forms Category Presence: PASSED")
        assert 'forms' in self.driver.current_url

    def test_alert_frame_windows_cat_click(self):
        self.homepage.click_alertFrameWindow()
        self.logger.info("AlertWindows Category Presence: PASSED")
        assert 'alertsWindows' in self.driver.current_url

    def test_widgets_cat_click(self):
        self.homepage.click_widgets()
        self.logger.info("Widgets Category Presence: PASSED")
        assert 'widgets' in self.driver.current_url

    def test_interactions_cat_click(self):
        self.homepage.click_interactions()
        self.logger.info("Interactions Category Presence: PASSED")
        assert 'interaction' in self.driver.current_url

    def test_books_app_cat_click(self):
        self.homepage.click_book_app()
        self.logger.info("Books APP Category Presence: PASSED")
        assert 'books' in self.driver.current_url

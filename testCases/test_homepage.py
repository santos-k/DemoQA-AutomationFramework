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
       - Click of the header image link.
       - Presence of footer text.
       - Number of categories displayed on the homepage.
       - Click of various categories like elements, forms, alerts and windows, widgets, interactions, and books app.
       """

    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.logger = GenerateLog.generate_log()

    @pytest.mark.sanity
    def test_page_loading(self):
        if self.driver.title == "DEMOQA":
            self.logger.info("Homepage title: PASSED")
            assert True
        else:
            self.logger.error("Homepage title: FAILED")
            assert False

    @pytest.mark.ui
    def test_logo_presence(self):
        self.header = self.homepage.get_header_element()
        if bool(self.header.find_element(By.TAG_NAME, "img")):
            self.logger.info("Header Logo Presence: PASSED")
            assert True
        else:
            self.logger.error("Header Logo Presence: FAILED")
            self.driver.save_screenshot(f".//Screenshots/{Test_WebElement.test_logo_presence.__name__}.png")
            assert False

    @pytest.mark.ui
    def test_logo_clickable(self):
        header = self.homepage.get_header_element()
        header.find_element(By.TAG_NAME, 'a').click()
        if self.driver.current_url == base_url and self.driver.title == "DEMOQA":
            self.logger.info("Logo is clickable: PASSED")
            assert True
        else:
            self.logger.error("Logo is clickable: FAILED")
            assert False

    @pytest.mark.ui
    def test_footer_presence(self):
        footer = self.homepage.get_footer_element()
        if bool(footer) and footer.text == self.homepage.footer_text:
            self.logger.info("Footer presence: PASSED")
            assert True
        else:
            self.logger.error("Footer presence: FAILED")
            assert False

    @pytest.mark.ui
    def test_nums_of_category(self):
        category_size, name_list = self.homepage.get_nums_of_category_and_names()
        if category_size == 6 and "Widgets" in name_list:
            self.logger.info("Categories Presence and number of categories also match: PASSED")
        else:
            self.logger.error("Categories Presence and number of categories also match: FAILED")

    @pytest.mark.parametrize("category, index", [
        ("Elements", 0),
        ("Forms", 1),
        ("AlertsWindows", 2),
        ("Widgets", 3),
        ("Interaction", 4),
        ("Books", 5)
    ])
    @pytest.mark.ui
    def test_category_click(self, category, index):
        self.homepage.click_category(index)
        if category.lower() in self.driver.current_url.lower():
            self.logger.info(f"{category} Category Presence and Clickable: PASSED")
            assert True
        else:
            self.logger.error(f"{category} Category Presence and Clickable: FAILED")
            assert False

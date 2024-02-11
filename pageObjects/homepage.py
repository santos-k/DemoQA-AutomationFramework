from selenium.webdriver.common.by import By


class Homepage:
    """
        This class represents the Homepage of the DEMOQA website and provides methods to interact with its elements.

        It includes methods for:
        - Retrieving the header element.
        - Retrieving the footer element.
        - Getting the number of categories displayed on the homepage and their names.
        - Clicking on various categories like elements, forms, alerts and windows, widgets, interactions, and books app.
        """

    header_tag_name = "header"
    footer_tag_name = "footer"
    home_banner_div_class = "home-banner"
    category_div_class = "category-cards"
    category_card_xpath = "//div[@class='card mt-4 top-card']"
    footer_text = "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."

    def __init__(self, driver):
        self.driver = driver

    def get_element_by_tag(self, tag_name):
        return self.driver.find_element(By.TAG_NAME, tag_name)

    def click_category(self, index):
        divs = self.driver.find_elements(By.XPATH, self.category_card_xpath)
        div = divs[index].find_elements(By.TAG_NAME, 'div')[0]
        self.driver.execute_script("arguments[0].click()", div)

    def get_header_element(self):
        return self.get_element_by_tag(self.header_tag_name)

    def get_footer_element(self):
        return self.get_element_by_tag(self.footer_tag_name)

    def get_nums_of_category_and_names(self):
        divs = self.driver.find_elements(By.XPATH, self.category_card_xpath)
        return len(divs), [div.text for div in divs]

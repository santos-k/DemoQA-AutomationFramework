import time

import pytest

from pageObjects.elements_page import Element_Page
from pageObjects.forms_page import Forms_Page
from pageObjects.homepage import Homepage


class Test_Form_Page:

    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_forms()
        self.elementpage = Element_Page(self.driver)
        self.elementpage.forms_page_open()
        self.formpage = Forms_Page(self.driver)

    def test_header_text(self):
        text = self.elementpage.get_header_text()
        assert "Practice Form" == text

    def test_forms(self):
        self.formpage.set_first_last_name("Santosh", "Kumar")
        self.formpage.set_gender('m')
        self.formpage.set_email_mobile('santosh@abc.com', 9999988888)
        self.formpage.set_hobbies(True,True,True)
        self.formpage.set_picture_address("C:\\Users\\withu\\Downloads\\python.png", "Rajiv Chowk, CP")
        # self.formpage.set_state_city(0,1)
        self.formpage.submit_form()
        time.sleep(20)


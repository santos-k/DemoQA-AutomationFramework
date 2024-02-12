import pytest
from pageObjects.elements_page import Element_Page
from pageObjects.forms_page import Forms_Page
from pageObjects.homepage import Homepage


class Test:
    menu_index, sub_menu_index = 1, 0

    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_category(1)
        self.elementpage = Element_Page(self.driver)
        self.elementpage.open_sub_menus(self.menu_index,self.sub_menu_index)
        self.formpage = Forms_Page(self.driver)


class Test_Form_Page(Test):
    def test_header_text(self):
        text = self.elementpage.get_header_text()
        assert "Practice Form" == text

    def test_forms(self):
        self.formpage.set_first_last_name("Santosh", "Kumar")
        self.formpage.set_gender('m')
        self.formpage.set_email_mobile('santosh@abc.com', 9999988888)
        # self.formpage.set_dob_subject("20 Feb 2024", "This is subject")
        self.formpage.set_hobbies(True,True, True)
        self.formpage.set_picture_address("C:\\Users\\withu\\Downloads\\python.png", "Rajiv Nagar, CP")
        self.formpage.submit_form()
        assert True

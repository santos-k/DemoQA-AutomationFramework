import pytest
from selenium.common import NoSuchElementException

from pageObjects.elements_page import Element_Page
from pageObjects.homepage import Homepage
from utilities.utils_functions import GenerateLog


class Test:
    menu_index, sub_menu_index = None, None

    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_category(0)
        self.element = Element_Page(self.driver)
        self.logger = GenerateLog.generate_log()
        if self.menu_index is not None:
            self.element.open_sub_menus(self.menu_index, self.sub_menu_index)


class Test_ElementPage(Test):
    @pytest.mark.ui
    def test_header_text(self):
        if self.element.get_header_text() == "Elements":
            self.logger.info("Elements Page Header Text: PASSED")
            assert True
        else:
            self.logger.error("Elements Page Header Text: FAILED")
            assert False

    @pytest.mark.ui
    def test_header_paragraph(self):
        expected = "Please select an item from left to start practice."
        if self.element.get_header_paragraph() == expected:
            self.logger.info("Elements Page summary text: PASSED")
            assert True
        else:
            self.logger.info("Elements Page summary text: FAILED")
            assert False

    @pytest.mark.ui
    def test_element_groups(self):
        groups = self.element.get_element_group()
        if "Text Box" in groups and len(groups) == 9:
            self.logger.info("Test Element groups: PASSED")
            assert True
        else:
            self.logger.info("Test Element groups: FAILED")
            assert False

    @pytest.mark.parametrize('element, index', [
        ('text-box', 0),
        ('checkbox', 1),
        ('radio-button', 2),
        ('webtables', 3),
        ('buttons', 4),
        ('links', 5),
        ('broken', 6),
        ('upload-download', 7),
        ('dynamic-properties', 8),
    ])
    @pytest.mark.ui
    def test_submenu_in_elements_clickable(self, element, index):
        self.element.click_sub_menu_element(0, index)
        if element in self.driver.current_url:
            self.logger.info(f"{element} clickable: PASSED")
            assert True, f"{element} not in url"
        else:
            self.logger.info(f"{element} clickable: FAILED")
            assert False


class Test_TextBox(Test):
    menu_index, sub_menu_index = 0, 0

    @pytest.mark.ui
    def test_verify_heading(self):
        assert "Text Box" == self.element.get_header_text(), "Heading text not matching"

    @pytest.mark.parametrize('name, email, cur_addr, per_addr', [
        ('Alex Zender', 'abc@gmail.com', '420, London', '421, London, England'),
        ('Hello', '', 'Patna', 'Gaya'),
        ('', 'peter.com', '420, London', '421, London, England'),
    ])
    @pytest.mark.regression
    def test_text_boxes_submission(self, name, email, cur_addr, per_addr):
        self.element.set_full_name_input(name)
        self.element.set_email_input(email)
        self.element.set_current_addr_input(cur_addr)
        self.element.set_permanent_addr_input(per_addr)
        self.element.click_submit_button()
        try:
            output = self.element.get_output_on_submit()
            for tag in [name, email, cur_addr, per_addr]:
                if len(tag) > 0:
                    assert tag in output
            self.logger.info("Text Box Submission with valid data: PASSED")
        except NoSuchElementException:
            try:
                self.logger.info("Text Box with invalid email format: PASSED")
                assert "error" in self.element.get_email_error()
            except NoSuchElementException:
                for tag in [name, email, cur_addr, per_addr]:
                    if len(tag) == 0:
                        self.logger.info("Text with empty string: PASSED")
                        assert True
                    else:
                        self.logger.error("Text with empty string: FAILED")
                        assert False


class Test_CheckBox(Test):
    menu_index, sub_menu_index = 0, 1

    @pytest.mark.regression
    def test_expand_all_check_boxes(self):
        self.element.expand_all_checkboxes().click()
        self.logger.info("Expend all CheckBoxes: PASSED")
        assert True

    @pytest.mark.regression
    def test_collapse_all_check_boxes(self):
        self.element.collapse_all_checkboxes().click()
        self.logger.info("Collapse all CheckBoxes: PASSED")
        assert True


class Test_Radio_Button(Test):
    menu_index, sub_menu_index = 0, 2

    @pytest.mark.regression
    @pytest.mark.parametrize("value", [('yes'), ('impressive'), ('no')])
    def test_radio_button(self, value):
        global result, radio
        try:
            radio = self.element.click_radio_button(value)
            result = self.element.get_message_on_radio_select()
        except Exception as e:
            print(e)
        if value == 'yes':
            assert 'Yes' == result
        elif value == 'impressive':
            assert 'Impressive' == result
        else:
            assert radio is False


class Test_Web_Tables(Test):
    menu_index, sub_menu_index = 0, 3

    @pytest.mark.regression
    def test_len_of_columns(self):
        col_list = self.element.get_table_columns_name()
        print("Columns in Table: ", col_list)
        assert "First Name" in col_list[0].split("\n")

    @pytest.mark.regression
    def test_data_in_table(self):
        data = self.element.get_table_rows_data()
        print("Data: ", data)
        assert len(data) > 0
        assert "Cierra" == data[0][0]
        assert '29' == data[2][2]

    @pytest.mark.regression
    def test_add_new_record_and_match(self):
        self.element.add_new_record_and_get('abc', 'abc',
                                            'abc@abc.com', 23,
                                            34343, 'QA')
        data = self.element.get_table_rows_data()
        assert 'abc' in data[3]
        assert 'abc@abc.com' in data[3][3]


class Test_Buttons_Click(Test):
    menu_index, sub_menu_index = 0, 4

    def test_right_click(self):
        self.element.right_click()
        msg = self.element.get_click_message('right')
        assert 'right' in msg, "Message not found"

    def test_double_click(self):
        self.element.double_click()
        msg = self.element.get_click_message('double')
        assert 'double' in msg, "Message not found"

    def test_click_home_link(self):
        self.element.click_home_link('Login')


class Test_Link_Clicks(Test):
    menu_index, sub_menu_index = 0, 5

    @pytest.mark.parametrize('link_text', [('Home'), ('Home3oQe8')])
    def test_home_link_click(self, link_text):
        self.element.click_home_link(link_text)
        assert self.driver.title == "DEMOQA", "Title not matched."

    @pytest.mark.parametrize('request_name',
                             [('Created'), ('No Content'), ('Moved'), ('Bad Request'), ('Unauthorized'), ('Forbidden'),
                              ('Not Found')])
    def test_links_sends_api_call(self, request_name):
        self.element.click_api_call_links(request_name)
        res_msg = self.element.get_api_response()
        assert request_name in res_msg


class Test_Upload_Download(Test):
    menu_index, sub_menu_index = 0, 6

    def test_download(self):
        self.element.upload_download('download', None)

    def test_upload(self):
        # file_path = "C:\\Automation\\Python\\DemoQA-Automation\\Screenshots\\test_logo_presence.png"
        uploaded_path = self.element.upload_download('upload', 'test_logo_presence.png')
        assert "test_logo_presence.png" in uploaded_path, "Failed to upload"

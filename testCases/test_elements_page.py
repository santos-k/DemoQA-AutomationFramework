import time

import pytest
from pageObjects.elements_page import Element_Page
from pageObjects.homepage import Homepage


class Test_ElementPage:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)

    def test_header_text(self):
        assert self.element.get_header_text() == "Elements", "Header text does not match"

    def test_header_paragraph(self):
        expected = "Please select an item from left to start practice."
        assert self.element.get_header_paragraph() == expected, "Header paragraph does not match"

    def test_element_groups(self):
        groups = self.element.get_element_group()
        assert "Text Box" in groups, "Text Box group not found"

    def test_click_text_box(self):
        self.element.click_text_box_sub_menu()
        assert "text-box" in self.driver.current_url, "Text Box URL not correct"

    def test_click_check_box(self):
        self.element.click_check_box_sub_menu()
        assert "checkbox" in self.driver.current_url, "Check Box URL not correct"


class Test_TextBox:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)
        self.element.click_text_box_sub_menu()

    def test_verify_heading(self):
        assert "Text Box" == self.element.get_header_text(), "Heading text not matching"

    def test_text_boxes_submission(self):
        self.element.set_full_name_input("Santosh Kumar")
        self.element.set_email_input("santosh@abc.com")
        self.element.set_current_addr_input("420, Chandni Chowk, Delhi")
        self.element.set_permanent_addr_input("840, Nehru Park, MP")
        self.element.click_submit_button()
        output = self.element.get_output_on_submit()
        assert "Santosh Kumar" in output, "Full name not in output"
        assert "santosh@abc.com" in output, "Email not in output"
        assert "error" not in self.element.get_email_error()


class Test_CheckBox:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)
        self.element.click_check_box_sub_menu()

    def test_expand_all_check_boxes(self):
        self.element.expand_all_checkboxes()
        assert True

    def test_collapse_all_check_boxes(self):
        self.element.collapse_all_checkboxes()
        assert True


class Test_Radio_Button:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)
        self.element.click_radio_button_sub_menu()

    @pytest.mark.parametrize("value", [('yes'), ('impressive'), ('no')])
    def test_radio_button(self, value):
        try:
            radio = self.element.click_radio_button(value)
            result = self.element.get_message_on_radio_select()
        except:
            pass
        if value == 'yes':
            assert 'Yes' == result
        elif value == 'impressive':
            assert 'Impressive' == result
        else:
            assert radio == False


class Test_Web_Tables:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)
        self.element.click_web_tables_sub_menu()

    def test_len_of_columns(self):
        col_list = self.element.get_table_columns_name()
        print("Columns in Table: ", col_list)
        assert "First Name" in col_list

    def test_data_in_table(self):
        data = self.element.get_table_rows_data()
        print("Data: ", data)
        assert len(data) > 0
        assert "Cierra" == data[0][0]
        assert '29' == data[2][2]

    def test_add_new_record_and_match(self):
        self.element.add_new_record_and_get('abc', 'abc',
                                            'abc@abc.com', 23,
                                            34343, 'QA')
        data = self.element.get_table_rows_data()
        assert 'abc' in data[3]
        assert 'abc@abc.com' in data[3][3]


class Test_Buttons_Click:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)
        self.element.click_buttons_sub_menu()

    def test_right_click(self):
        self.element.right_click()
        msg = self.element.get_click_message('right')
        assert 'right' in msg, "Message not found"

    def test_double_click(self):
        self.element.double_click()
        msg = self.element.get_click_message('double')
        assert 'double' in msg, "Message not found"


    def test_click_home_link(self):
        self.element.click_home_link()


class Test_Link_Clicks:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)
        self.element.click_links_sub_menu()

    @pytest.mark.parametrize('link_text',[('Home'), ('Home3oQe8')])
    def test_home_link_click(self, link_text):
        self.element.click_home_link(link_text)
        assert self.driver.title == "DEMOQA", "Title not matched."

    @pytest.mark.parametrize('request_name',[('Created'),('No Content'), ('Moved'),('Bad Request'), ('Unauthorized'), ('Forbidden'), ('Not Found')])
    def test_links_sends_api_call(self, request_name):
        self.element.click_api_call_links(request_name)
        res_msg = self.element.get_api_response()
        assert request_name in res_msg


class Test_Upload_Download:
    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_elements()
        self.element = Element_Page(self.driver)
        self.element.click_upload_download_sub_menu()

    def test_download(self):
        self.element.upload_download('download',None)

    def test_upload(self):
        file_path = "C:\\Automation\\Python\\DemoQA-Automation\\Screenshots\\test_logo_presence.png"
        uploaded_path = self.element.upload_download('upload', 'test_logo_presence.png')
        assert "test_logo_presence.png" in uploaded_path, "Failed to upload"

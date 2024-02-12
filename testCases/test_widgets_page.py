import time
import pytest
from selenium.webdriver.common.by import By
from pageObjects.homepage import Homepage
from pageObjects.widgets_page import Widgets_Page
from pageObjects.elements_page import Element_Page


class Test:
    menu_index = None
    sub_menu_index = None

    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_category(3)
        self.elementpage = Element_Page(self.driver)
        self.elementpage.open_sub_menus(self.menu_index, self.sub_menu_index)
        self.widgets = Widgets_Page(self.driver)


class Test_Accordian(Test):
    menu_index, sub_menu_index = 3, 0

    def test_accordian_heading(self):
        assert "Accordian" == self.elementpage.get_header_text()

    @pytest.mark.parametrize("index, exp_heading, exp_body",
                             [(0, "What is Lorem Ipsum?", "Lorem Ipsum"),
                              (1, "Where does it come from?", "Contrary to popular belief"),
                              (2, "Why do we use it?", "It is a long established fact that a reader")])
    def test_accordian(self, index, exp_heading, exp_body):
        heading_text, body_text = self.widgets.get_accordian(index)
        assert exp_heading == heading_text
        assert exp_body in body_text


class Test_Auto_Complete(Test):
    menu_index, sub_menu_index = 3, 1

    def test_auto_complete(self):
        pass


class Test_Date_Picker(Test):
    menu_index, sub_menu_index = 3, 2

    def test_date_picker(self):
        date = "20/09/2025"
        date_picker_element = self.driver.find_element(By.ID, self.widgets.date_picker_id)
        self.widgets.set_date(date)
        time.sleep(1)
        actual_date = date_picker_element.get_attribute('value')
        assert date == actual_date

    def test_datetime_picker(self):
        datetime = "February 12, 2032 5:36 PM"
        value = self.driver.find_element(By.ID, self.widgets.date_n_time_picker_id)
        self.widgets.set_datetime(datetime)
        time.sleep(1)
        actual_datime = value.get_attribute('value')
        assert datetime == actual_datime


# Range Slider Page
class Test_Range_Slider(Test):
    menu_index, sub_menu_index = 3, 3

    def test_range_slider(self):
        self.widgets.set_range_slider_value(55)
        actual_value = self.driver.find_element(By.ID, self.widgets.range_value_display_id).get_attribute('value')
        assert 55 == int(actual_value)


class Test_Progress_Bar(Test):
    menu_index, sub_menu_index = 3, 4

    def test_progress_bar(self):
        self.widgets.set_progress_bar(3)
        assert True


class Test_Tabs(Test):
    menu_index, sub_menu_index = 3, 5

    @pytest.mark.parametrize("tab_name,expt_result", [('what', 'Lorem Ipsum is simply dummy text'),
                                                      ('use', 'It is a long established fact that a reader'),
                                                      ('origin', 'Contrary to popular belief, Lorem Ipsum')])
    def test_tabs(self, tab_name, expt_result):
        self.widgets.click_tabs(tab_name)
        time.sleep(1)
        content = self.widgets.get_active_tab_content()
        assert expt_result in content


class Test_ToolTips(Test):
    menu_index, sub_menu_index = 3, 6

    def test_tool_tip_on_btn(self):
        msg = self.widgets.get_tool_tip_on_btn_msg()
        assert "You hovered over the Button" == msg

    def test_tool_tip_on_input_field(self):
        msg = self.widgets.get_tool_tip_on_input_field_msg()
        assert "You hovered over the text field" == msg


class Test_Menus(Test):
    menu_index, sub_menu_index = 3, 7

    def test_menu_item1_click(self):
        href = self.widgets.click_menu_item1()
        assert href == 'https://demoqa.com/menu#'

    def test_hover_menu2(self):
        self.widgets.test_hover_menu()


class Test_Select_Menu(Test):
    menu_index, sub_menu_index = 3, 8

    def test_select_value_field(self):
        text = self.widgets.select_value_dropdown()
        assert text == "Group 1, option 2"

    def test_old_style_select_menu(self):
        text = self.widgets.old_style_menu_style("Yellow")
        assert text == 'Yellow'

    def test_multiselect_dropdown(self):
        try:
            self.widgets.multiselect_dropdown()
            assert True
        except:
            assert False

    def test_standard_multiselect(self):
        lists = self.widgets.standard_multiselect()
        assert lists == ['Volvo', 'Saab', 'Opel']

import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.elements_page import Element_Page
from pageObjects.homepage import Homepage
from pageObjects.alert_form_windows_page import Alert_Frame_Widows_Page


class Test_Windows:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elementpage = Element_Page(self.driver)
        self.elementpage.open_sub_menus(2,0)
        self.alertpage = Alert_Frame_Widows_Page(self.driver)

    def test_header_text(self):
        assert self.elementpage.get_header_text() == "Browser Windows"

    def test_open_new_tab(self):
        self.alertpage.open_new_tab()

        # Before switching to new tab
        assert "DEMOQA" == self.driver.title
        assert "https://demoqa.com/browser-windows" == self.driver.current_url

        # Switch to new tab
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])
        assert "" == self.driver.title
        assert "https://demoqa.com/sample" == self.driver.current_url

    def test_open_new_window(self):
        self.alertpage.open_new_window()
        # Before switching to new tab
        assert "DEMOQA" == self.driver.title
        assert "https://demoqa.com/browser-windows" == self.driver.current_url

        # Switch to new tab
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])
        assert "" == self.driver.title
        assert "https://demoqa.com/sample" == self.driver.current_url

    def test_open_new_window_message(self):
        self.alertpage.open_new_window_message()

class Test_Alerts:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elementpage = Element_Page(self.driver)
        self.elementpage.open_sub_menus(2, 1)
        self.alertpage = Alert_Frame_Widows_Page(self.driver)

    def test_alert(self):
        self.alertpage.click_alert_button()
        alert = self.driver.switch_to.alert
        alert.accept()
        assert "You clicked a button" == alert.text

    def test_alert_dalay(self):
        self.alertpage.click_delay_alert_button()
        time.sleep(5)
        delay = self.driver.switch_to.alert
        delay.accept()
        assert "This alert appeared after 5 seconds" == delay.text

    @pytest.mark.parametrize('act', [('accept'), ('dismiss')])
    def test_confirm_alert(self, act):
        self.alertpage.click_confirm_button()
        confirm = self.driver.switch_to.alert
        assert "Do you confirm action?" == confirm.text
        if act == "accept":
            confirm.accept()
            msg = self.alertpage.get_confirm_result()
            assert "You selected Ok" == msg
        elif act == "dismiss":
            confirm.dismiss()
            msg = self.alertpage.get_confirm_result()
            assert "You selected Cancel" == msg

    @pytest.mark.parametrize('act', [('accept'), ('dismiss')])
    def test_prompt(self, act):
        self.alertpage.click_prompt()
        prompt = self.driver.switch_to.alert
        msg = prompt.text
        assert "Please enter your name" == msg
        if act == 'accept':
            prompt.send_keys("Hello Peter")
            prompt.accept()
            msg = self.alertpage.get_prompt_result()
            assert msg == "You entered Hello Peter"
        elif act == 'dismiss':
            prompt.dismiss()
            assert True


class Test_Frames:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elementpage = Element_Page(self.driver)
        self.elementpage.open_sub_menus(2, 2)
        self.alertpage = Alert_Frame_Widows_Page(self.driver)

    def test_frames_header_text(self):
        assert self.elementpage.get_header_text() == "Frames"

    def test_large_frame(self):
        self.driver.switch_to.frame(self.alertpage.large_frame_id)
        text = self.alertpage.get_large_frame_content()
        assert text == "This is a sample page"

    def test_small_frame(self):
        self.driver.switch_to.frame(self.alertpage.small_frame_id)
        text = self.alertpage.get_small_frame_content()
        assert text == "This is a sample page"


class Test_Nested_Frames:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elementpage = Element_Page(self.driver)
        self.elementpage.open_sub_menus(2, 3)
        self.alertpage = Alert_Frame_Widows_Page(self.driver)

    def test_parent_frame(self):
        self.driver.switch_to.frame(self.alertpage.parent_frame_id)
        content = self.alertpage.get_parent_frame_content()
        assert "Parent frame" == content

        self.driver.switch_to.frame(0)
        content = self.alertpage.get_parent_frame_content()
        assert "Child Iframe" == content


class Test_Models:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elementpage = Element_Page(self.driver)
        self.elementpage.open_sub_menus(2, 4)
        self.alertpage = Alert_Frame_Widows_Page(self.driver)

    def test_model_page_header_text(self):
        assert "Modal Dialogs" == self.elementpage.get_header_text()

    def test_small_model(self):
        self.alertpage.get_small_model()
        title = self.alertpage.get_model_title()
        body = self.alertpage.get_model_body_text()
        assert "Small Modal" in title
        assert "small modal" in body
        self.alertpage.close_model_by_btn('s')

    def test_large_model(self):
        self.alertpage.get_large_model()
        body = self.alertpage.get_model_body_text()
        assert "Lorem Ipsum is simply dummy text" in body
        self.alertpage.close_model_by_btn('l')

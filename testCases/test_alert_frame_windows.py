import time
import pytest
from pageObjects.elements_page import Element_Page
from pageObjects.homepage import Homepage
from pageObjects.alert_form_windows_page import Alert_Frame_Widows_Page


class Test:
    menu_index, sub_menu_index = None, None

    @pytest.fixture(autouse=True)
    def init_test(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elements_page = Element_Page(self.driver)
        self.elements_page.open_sub_menus(self.menu_index, self.sub_menu_index)
        self.alert_page = Alert_Frame_Widows_Page(self.driver)


class Test_Windows(Test):
    menu_index, sub_menu_index = 2, 0

    def test_header_text(self):
        assert self.elements_page.get_header_text() == "Browser Windows"

    def test_open_new_tab(self):
        self.alert_page.open_new_tab()

        # Before switching to new tab
        assert "DEMOQA" == self.driver.title
        assert "https://demoqa.com/browser-windows" == self.driver.current_url

        # Switch to new tab
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])
        assert "" == self.driver.title
        assert "https://demoqa.com/sample" == self.driver.current_url

    def test_open_new_window(self):
        self.alert_page.open_new_window()
        # Before switching to new tab
        assert "DEMOQA" == self.driver.title
        assert "https://demoqa.com/browser-windows" == self.driver.current_url

        # Switch to new tab
        win_handles = self.driver.window_handles
        self.driver.switch_to.window(win_handles[1])
        assert "" == self.driver.title
        assert "https://demoqa.com/sample" == self.driver.current_url

    def test_open_new_window_message(self):
        self.alert_page.open_new_window_message()


class Test_Alerts(Test):
    menu_index, sub_menu_index = 2, 1

    def test_alert(self):
        self.alert_page.click_alert_button()
        alert = self.driver.switch_to.alert
        alert.accept()
        assert "You clicked a button" == alert.text

    def test_alert_delay(self):
        self.alert_page.click_delay_alert_button()
        time.sleep(6)
        delay = self.driver.switch_to.alert
        delay.accept()
        assert "This alert appeared after 5 seconds" == delay.text

    @pytest.mark.parametrize('act', [('accept'), ('dismiss')])
    def test_confirm_alert(self, act):
        self.alert_page.click_confirm_button()
        confirm = self.driver.switch_to.alert
        assert "Do you confirm action?" == confirm.text
        if act == "accept":
            confirm.accept()
            msg = self.alert_page.get_confirm_result()
            assert "You selected Ok" == msg
        elif act == "dismiss":
            confirm.dismiss()
            msg = self.alert_page.get_confirm_result()
            assert "You selected Cancel" == msg

    @pytest.mark.parametrize('act', [('accept'), ('dismiss')])
    def test_prompt(self, act):
        self.alert_page.click_prompt()
        prompt = self.driver.switch_to.alert
        msg = prompt.text
        assert "Please enter your name" == msg
        if act == 'accept':
            prompt.send_keys("Hello Peter")
            prompt.accept()
            msg = self.alert_page.get_prompt_result()
            assert msg == "You entered Hello Peter"
        elif act == 'dismiss':
            prompt.dismiss()
            assert True


class Test_Frames(Test):
    menu_index, sub_menu_index = 2, 2

    def test_frames_header_text(self):
        assert self.elements_page.get_header_text() == "Frames"

    def test_large_frame(self):
        self.driver.switch_to.frame(self.alert_page.large_frame_id)
        text = self.alert_page.get_large_frame_content()
        assert text == "This is a sample page"

    def test_small_frame(self):
        self.driver.switch_to.frame(self.alert_page.small_frame_id)
        text = self.alert_page.get_small_frame_content()
        assert text == "This is a sample page"


class Test_Nested_Frames(Test):
    menu_index, sub_menu_index = 2, 3

    def test_parent_frame(self):
        self.driver.switch_to.frame(self.alert_page.parent_frame_id)
        content = self.alert_page.get_parent_frame_content()
        assert "Parent frame" == content

        self.driver.switch_to.frame(0)
        content = self.alert_page.get_parent_frame_content()
        assert "Child Iframe" == content


class Test_Models(Test):
    menu_index, sub_menu_index = 2, 4

    def test_model_page_header_text(self):
        assert "Modal Dialogs" == self.elements_page.get_header_text()

    def test_small_model(self):
        self.alert_page.get_small_model()
        title = self.alert_page.get_model_title()
        body = self.alert_page.get_model_body_text()
        assert "Small Modal" in title
        assert "small modal" in body
        self.alert_page.close_model_by_btn('s')

    def test_large_model(self):
        self.alert_page.get_large_model()
        body = self.alert_page.get_model_body_text()
        assert "Lorem Ipsum is simply dummy text" in body
        self.alert_page.close_model_by_btn('l')

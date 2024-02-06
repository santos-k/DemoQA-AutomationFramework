from selenium.webdriver.common.by import By


class Alert_Frame_Widows_Page:
    # Window Page
    open_new_tab_button_id = "tabButton"
    open_new_window_button_id = "windowButton"
    open_new_window_message_button_id = "messageWindowButton"

    # Alert Page
    alert_button_id = "alertButton"
    alert_delay_button_id = "timerAlertButton"
    confirm_button_id = "confirmButton"
    prompt_button_id = "promtButton"
    confirm_click_result_id = "confirmResult"
    prompt_click_result_id = "promptResult"

    # Frames
    large_frame_id = "frame1"
    small_frame_id = "frame2"

    # Nested Frames
    parent_frame_id = "frame1"

    # Models
    show_small_model_btn_id = "showSmallModal"
    show_large_model_btn_id = "showLargeModal"
    model_div_class = "modal-content"
    model_title_class = "modal-title"
    model_x_btn_close_class = "close"
    model_body_class = "modal-body"
    close_large_model_btn_id = "closeLargeModal"
    close_small_model_btn_id = "closeSmallModal"

    def __init__(self, driver):
        self.driver = driver

    def open_new_tab(self):
        self.driver.find_element(By.ID, self.open_new_tab_button_id).click()

    def open_new_window(self):
        self.driver.find_element(By.ID, self.open_new_window_button_id).click()

    def open_new_window_message(self):
        self.driver.find_element(By.ID, self.open_new_window_message_button_id).click()

    # Alert Page
    def click_alert_button(self):
        self.driver.find_element(By.ID, self.alert_button_id).click()

    def click_delay_alert_button(self):
        self.driver.find_element(By.ID, self.alert_delay_button_id).click()

    def click_confirm_button(self):
        self.driver.find_element(By.ID, self.confirm_button_id).click()

    def click_prompt(self):
        prompt_btn = self.driver.find_element(By.ID, self.prompt_button_id)
        self.driver.execute_script("arguments[0].click()",prompt_btn)

    def get_confirm_result(self):
        return self.driver.find_element(By.ID, self.confirm_click_result_id).text

    def get_prompt_result(self):
        return self.driver.find_element(By.ID, self.prompt_click_result_id).text

    # Frames page
    def get_large_frame_content(self):
        return self.driver.find_element(By.TAG_NAME, 'h1').text

    def get_small_frame_content(self):
        return self.driver.find_element(By.TAG_NAME, 'h1').text

    # Nested Frames page
    def get_parent_frame_content(self):
        return self.driver.find_element(By.TAG_NAME, 'body').text

    # Models page
    def get_small_model(self):
        self.driver.find_element(By.ID, self.show_small_model_btn_id).click()

    def get_large_model(self):
        self.driver.find_element(By.ID, self.show_large_model_btn_id).click()

    def get_model_title(self):
        return self.driver.find_element(By.CLASS_NAME, self.model_title_class).text

    def get_model_body_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.model_body_class).text

    def close_model_from_header_x_btn(self):
        self.driver.find_element(By.CLASS_NAME, self.model_x_btn_close_class).click()

    def close_model_by_btn(self, n):
        """
        :param n: str | ['l' for large button or 's' for small button]
        :return:
        """
        if n == 'l':
            self.driver.find_element(By.ID, self.close_large_model_btn_id).click()
        elif n == 's':
            self.driver.find_element(By.ID, self.close_small_model_btn_id).click()
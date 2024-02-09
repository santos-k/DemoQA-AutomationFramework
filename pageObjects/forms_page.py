from selenium import webdriver
from selenium.webdriver.common.by import By


class Forms_Page:
    fname_input_id = "firstName"
    lname_input_id = "lastName"
    email_input_id = "userEmail"

    male_gender_radio_id = "gender-radio-1"
    female_gender_radio_id = "gender-radio-2"
    other_gender_radio_id = "gender-radio-3"

    mobile_number_input_id = "userNumber"
    dob_input_id = "dateOfBirthInput"
    subject_input_id = "subjectsInput"

    sports_hobbies_checkbox_id = "hobbies-checkbox-1"
    reading_hobbies_checkbox_id = "hobbies-checkbox-2"
    music_hobbies_checkbox_id = "hobbies-checkbox-3"
    upload_picture_input_id = "uploadPicture"

    current_addr_textarea_id = "currentAddress"
    state_dropdown_id = "state"
    city_dropdown_id = "city"

    dropdown_options_xpath = "//div[@class=' css-11unzgr']"
    submit_button_id = "submit"

    def __init__(self, driver):
        self.driver = driver

    def set_first_last_name(self, f, l):
        self.driver.find_element(By.ID, self.fname_input_id).send_keys(f)
        self.driver.find_element(By.ID, self.lname_input_id).send_keys(l)

    def set_gender(self, g):
        if g == 'm':
            male = self.driver.find_element(By.ID, self.male_gender_radio_id)
            self.driver.execute_script("arguments[0].click()", male)
        elif g == 'f':
            female = self.driver.find_element(By.ID, self.female_gender_radio_id)
            self.driver.execute_script("arguments[0].click()", female)
        elif g == 'o':
            other = self.driver.find_element(By.ID, self.other_gender_radio_id)
            self.driver.execute_script("arguments[0].click()", other)
        else:
            pass

    def set_email_mobile(self, email,mobile):
        self.driver.find_element(By.ID, self.email_input_id).send_keys(email)
        self.driver.find_element(By.ID, self.mobile_number_input_id).send_keys(mobile)

    def set_dob_subject(self, dob, sub):
        date = (self.driver.find_element(By.ID, self.dob_input_id).clear())
        date.send_keys(dob)
        self.driver.find_element(By.ID, self.subject_input_id).send_keys(sub)

    def set_hobbies(self, s=False, m=False, r=False):
        checkboxes = {
            'sports': (self.sports_hobbies_checkbox_id, s),
            'music': (self.music_hobbies_checkbox_id, m),
            'reading': (self.reading_hobbies_checkbox_id, r)
        }

        for hobby, (checkbox_id, flag) in checkboxes.items():
            checkbox = self.driver.find_element(By.ID, checkbox_id)
            if flag != checkbox.is_selected():
                self.driver.execute_script("arguments[0].click()", checkbox)

    def set_picture_address(self, filepath, addr):
        self.driver.find_element(By.ID, self.upload_picture_input_id).send_keys(filepath)
        self.driver.find_element(By.ID, self.current_addr_textarea_id).send_keys(addr)

    def set_state_city(self, state_index, city_index):
        state_dropdown = self.driver.find_element(By.XPATH, self.state_dropdown_id).click()
        state_dropdown.click()
        option_div = self.driver.find_element(By.XPATH, self.dropdown_options_xpath)
        options = option_div.find_elements(By.TAG_NAME, 'div')
        options[state_index].click()

        state_dropdown = self.driver.find_element(By.XPATH, self.city_dropdown_id).click()
        state_dropdown.click()
        option_div = self.driver.find_element(By.XPATH, self.dropdown_options_xpath)
        options = option_div.find_elements(By.TAG_NAME, 'div')
        options[city_index].click()

    def submit_form(self):
        submit = self.driver.find_element(By.ID, self.submit_button_id)
        self.driver.execute_script('arguments[0].click()', submit)






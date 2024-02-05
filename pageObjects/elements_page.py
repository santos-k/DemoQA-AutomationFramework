import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Element_Page:
    main_header_text_class = "main-header"  # Main element category heading
    text_id = "Ad.Plus-728x90"  # text to start
    accordian_class = "accordion"  # inside this div all element category list present
    elements_group_div_class = "element-group"  # inside this group header and element-list present
    groups_header_span_class = "group-header"  # inside this element header name text and collapse button present
    groups_element_div_class = "element-list"  # div of ul
    element_list_ul_class = "menu-list"  # ul of list of  all elements belongs

    # Elements on Text Box Page:
    username_input_css = "input#userName"
    email_input_css = "input#userEmail"
    current_address_textarea_css = "textarea#currentAddress"
    permanent_address_textarea_css = "textarea#permanentAddress"
    submit_button_css = "button#submit"
    output_div_id = "output"

    # Elements on Check Box Page
    CheckBox_main_div_class = "react-checkbox-tree"
    expand_all_checkboxes_button_class = "rct-option-expand-all"
    collapse_all_checkboxes_button_class = "rct-option-collapse-all"
    check_all_boxes_class = "rct-checkbox"

    # Elements on Radio Button page
    yes_radio_btn_css = "#yesRadio"
    impressive_radio_btn_css = "#impressiveRadio"
    no_radio_btn_css = "#noRadio"   # disabled
    msg_on_radio_select_class = "text-success"

    # Elements on Web Tables page
    add_new_record_button_id = "addNewRecordButton"
    search_box_input_id = "searchBox"
    table_rows_data_class = "rt-tr-group"
    form_id = "userForm"
    first_name_id = "firstName"
    last_name_id = "lastName"
    email_id = "userEmail"
    age_id = "age"
    salary_id = "salary"
    department_id = "department"
    submit_button_id = "submit"

    # Elements on Buttons page
    double_click_btn_id = "doubleClickBtn"
    right_click_btn_id = "rightClickBtn"
    dynamic_click_btn_id = "Dkj0l"
    double_click_message_id = "doubleClickMessage"
    right_click_message_id = "rightClickMessage"
    dynamic_click_message_id = "dynamicClickMessage"

    # Elements on Links page
    home_link_id = "simpleLink"
    home_link_Text = "Home"
    api_response_id = "linkResponse"

    # Upload And Download
    download_btn_id = "downloadButton"
    upload_id = "uploadFile"
    upload_file_path_id = "uploadedFilePath"

    def __init__(self, driver):
        self.driver = driver
        self.act = ActionChains(self.driver)

    def get_header_text(self):
        return self.driver.find_element(By.CLASS_NAME, self.main_header_text_class).text

    def get_header_paragraph(self):
        return self.driver.find_element(By.ID, self.text_id).text

    def get_element_group(self):
        menus = self.driver.find_elements(By.CLASS_NAME, self.elements_group_div_class)
        sub_menu = menus[0].find_element(By.CLASS_NAME, self.element_list_ul_class)
        menu_list = sub_menu.find_elements(By.TAG_NAME, 'li')
        return [menu.text for menu in menu_list]

    def click_sub_menu_element(self, menu_element_index, sub_menu_id_index):
        menus = self.driver.find_elements(By.CLASS_NAME, self.elements_group_div_class)
        sub_menu = menus[menu_element_index].find_element(By.CLASS_NAME, self.element_list_ul_class)
        menu_list = sub_menu.find_elements(By.TAG_NAME, 'li')
        self.driver.execute_script("arguments[0].click()", menu_list[sub_menu_id_index])

    def click_text_box_sub_menu(self):
        self.click_sub_menu_element(0, 0)

    def click_check_box_sub_menu(self):
        self.click_sub_menu_element(0, 1)

    def click_radio_button_sub_menu(self):
        self.click_sub_menu_element(0, 2)

    def click_web_tables_sub_menu(self):
        self.click_sub_menu_element(0, 3)

    def click_buttons_sub_menu(self):
        self.click_sub_menu_element(0, 4)

    def click_links_sub_menu(self):
        self.click_sub_menu_element(0, 5)

    def click_broken_links_sub_menu(self):
        self.click_sub_menu_element(0, 6)

    def click_upload_download_sub_menu(self):
        self.click_sub_menu_element(0, 7)

    def click_dynamic_properties_sub_menu(self):
        self.click_sub_menu_element(0, 8)

    # For Forms page
    def forms_page_open(self):
        self.click_sub_menu_element(1, 0)

    # Text Boxes methods
    def set_full_name_input(self, full_name):
        self.driver.find_element(By.CSS_SELECTOR, self.username_input_css).send_keys(full_name)

    def set_email_input(self, email):
        email_element = self.driver.find_element(By.CSS_SELECTOR, self.email_input_css)
        self.driver.execute_script("arguments[0].value = arguments[1];", email_element, email)

    def get_email_error(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.email_input_css).get_attribute('class')

    def set_current_addr_input(self, current_addr):
        self.driver.find_element(By.CSS_SELECTOR, self.current_address_textarea_css).send_keys(current_addr)

    def set_permanent_addr_input(self, permanent_addr):
        permanent_addr_element = self.driver.find_element(By.CSS_SELECTOR, self.permanent_address_textarea_css)
        self.driver.execute_script("arguments[0].value = arguments[1];", permanent_addr_element, permanent_addr)

    def get_output_on_submit(self):
        time.sleep(2)
        name = self.driver.find_element(By.CSS_SELECTOR, "p#name").text
        email = self.driver.find_element(By.CSS_SELECTOR, "p#email").text
        curAddr = self.driver.find_element(By.CSS_SELECTOR, "p#currentAddress").text
        perAddr = self.driver.find_element(By.CSS_SELECTOR, "p#permanentAddress").text
        return name + email + curAddr + perAddr

    def click_submit_button(self):
        submit = self.driver.find_element(By.CSS_SELECTOR, self.submit_button_css)
        self.driver.execute_script("arguments[0].click()", submit)

    # Check Box Methods
    def expand_all_checkboxes(self):
        self.driver.find_element(By.CLASS_NAME, self.expand_all_checkboxes_button_class).click()

    def collapse_all_checkboxes(self):
        self.driver.find_element(By.CLASS_NAME, self.collapse_all_checkboxes_button_class).click()

    # Radio Button methods
    def click_radio_button(self, value):
        """
        :param value: valid values ['yes', 'impressive','no']
        :return: None
        """
        if value.lower() == "yes":
            yes_radio = self.driver.find_element(By.CSS_SELECTOR, self.yes_radio_btn_css)
            self.driver.execute_script("arguments[0].click()", yes_radio)
        elif value.lower() == "impressive":
            impressive_radio = self.driver.find_element(By.CSS_SELECTOR, self.impressive_radio_btn_css)
            self.driver.execute_script("arguments[0].click()", impressive_radio)
        elif value.lower() == 'no':
            return self.driver.find_element(By.CSS_SELECTOR, self.no_radio_btn_css).is_enabled()
        else:
            raise "Invalid input"

    def get_message_on_radio_select(self):
        return self.driver.find_element(By.CLASS_NAME, self.msg_on_radio_select_class).text

    # Methods for web tables elements
    def get_table_columns_name(self):
        columns = self.driver.find_elements(By.XPATH, self.table_columns_xpath)
        return [column.text for column in columns]

    def get_table_rows_data(self):
        data = {}
        rows = self.driver.find_elements(By.CLASS_NAME, self.table_rows_data_class)
        for index, row in enumerate(rows):
            data[index] = row.text.split("\n")
        return data

    def add_new_record_and_get(self,fname,lname,email,age,salary,dept):
        """

        :param fname: str
        :param lname: str
        :param email: str|email
        :param age: int
        :param salary: float
        :param dept: str
        :return: None
        """
        self.driver.find_element(By.ID, self.add_new_record_button_id).click()
        form = self.driver.find_element(By.ID, self.form_id)
        form.find_element(By.ID, self.first_name_id).send_keys(fname)
        form.find_element(By.ID, self.last_name_id).send_keys(lname)
        form.find_element(By.ID, self.email_id).send_keys(email)
        form.find_element(By.ID, self.age_id).send_keys(age)
        form.find_element(By.ID, self.salary_id).send_keys(salary)
        form.find_element(By.ID, self.department_id).send_keys(dept)
        submit = form.find_element(By.ID, "submit")
        self.driver.execute_script("arguments[0].click()", submit)

    # Buttons Methods:
    def double_click(self):
        double_btn = self.driver.find_element(By.ID, self.double_click_btn_id)
        self.act.double_click(double_btn).perform()

    def right_click(self):
        right_btn = self.driver.find_element(By.ID, self.right_click_btn_id)
        self.act.context_click(right_btn).perform()

    def get_click_message(self, nclick):
        message = None
        if nclick == 'double':
            message = self.driver.find_element(By.ID, self.double_click_message_id).text
        elif nclick == 'right':
            message = self.driver.find_element(By.ID, self.right_click_message_id).text
        elif nclick == 'dynamic':
            message = self.driver.find_element(By.ID, self.dynamic_click_message_id).text
        return message

    def click_home_link(self, link_text):
        self.driver.find_element(By.LINK_TEXT, link_text).click()

    def click_api_call_links(self, link_text):
        click_link = self.driver.find_element(By.LINK_TEXT, link_text)
        self.driver.execute_script("arguments[0].click()", click_link)

    def get_api_response(self):
        return self.driver.find_element(By.ID, self.api_response_id).text

    def upload_download(self, n, file):
        if n == 'upload':
            self.driver.find_element(By.ID, self.upload_id).send_keys(file)
            return self.driver.find_element(By.ID, self.upload_file_path_id).text
        elif n == 'download':
            self.driver.find_element(By.ID, self.download_btn_id).click()
        else:
            pass
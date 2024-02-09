import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Widgets_Page:
    # Accordian Page
    accordian_div_id = "accordianContainer"  # 3 cards in this div
    accordian_card_class = "card"  # 3 cards
    accordian_card_heading_class = "card-header"  # click this to expand and collapse
    accordian_card_collapse_class = "collapse"  # check if this class has 'collapse show' then body will be visible if 'collapse' then not visible
    accordian_card_body_class = "card-body"

    # Auto Complete Dropdown
    auto_complete_multiple_input_id = "autoCompleteMultipleInput"
    auto_complete_multiple_list_class = "auto-complete__menu-list--is-multi"
    auto_complete_single_input = "autoCompleteSingleInput"

    # Date Picker
    date_picker_id = "datePickerMonthYearInput"  # 02/06/2024
    date_n_time_picker_id = "dateAndTimePickerInput"  # "February 6, 2024 7:30 PM"

    # Range Slider
    range_slider_input_xpath = "//input[@class='range-slider range-slider--primary']"
    range_value_display_id = "sliderValue"

    # Progress bar
    progress_bar_div = "//*[@class='progress-bar bg-info']"
    start_stop_btn_id = "startStopButton"

    # Tabs
    what_tab_id = "demo-tab-what"
    origin_tab_id = "demo-tab-origin"
    use_tab_id = "demo-tab-use"
    more_tab_id = "demo-tab-more"
    tab_content_div_class = "tab-pane"

    # Tool tips
    tool_tip_btn_id = "toolTipButton"
    btn_tool_tip_msg_div_class = "tooltip-inner"
    text_field_id = "texFieldToolTopContainer"

    # Menu
    menu_item1_link_text = "Main Item 1"
    menu_item2_link_text = "Main Item 1"
    menu_item2_sub_item_link_text = "Sub Item" # 2 sub items in menu item 2
    menu_item2_sub_item_list_link_text = "SUB SUB LIST »"
    menu_item2_sub_item_list1_link_text = "Sub Sub Item 1"
    menu_item2_sub_item_list2_link_text = "Sub Sub Item 2"

    # Select Menu
    dropdown_list_btn_xpath = "//div[@class=' css-tlfecz-indicatorContainer']" # common for all
    group1_option1_id = "react-select-2-option-0-0"
    group1_option2_id = "react-select-2-option-0-1"
    group2_option1_id = "react-select-2-option-1-0"
    group2_option2_id = "react-select-2-option-1-1"
    a_root_option_id = "react-select-2-option-2"

    pick_one_title_option_id = "react-select-6-group-0-heading"
    dr_option_id = "react-select-6-option-0-0"
    mr_option_id = "react-select-6-option-0-1"
    mrs_option_id = "react-select-6-option-0-2"
    ms_option_id = "react-select-6-option-0-3"
    prof_option_id = "react-select-6-option-0-4"
    other_option_id = "react-select-6-option-0-5"
    another_root_option_id = "react-select-2-option-3"

    old_style_select_dropdown_id = "oldSelectMenu"

    green_color_multi_select_id = "react-select-4-option-0"
    blue_color_multi_select_id = "react-select-4-option-1"
    black_color_multi_select_id = "react-select-4-option-2"
    red_color_multi_select_id = "react-select-4-option-3"

    def __init__(self, driver):
        self.driver = driver
        self.act = ActionChains(self.driver)

    def get_accordian(self, index):
        card_body = None
        accordian = self.driver.find_element(By.ID, self.accordian_div_id)
        cards = accordian.find_elements(By.CLASS_NAME, self.accordian_card_class)
        card = cards[index]
        card_heading = card.find_element(By.CLASS_NAME, self.accordian_card_heading_class)
        collapse_class_value = card.find_element(By.CLASS_NAME, 'collapse').get_attribute('class')
        if collapse_class_value == 'collapse show':
            card_body = card.find_element(By.CLASS_NAME, self.accordian_card_body_class).text
        elif collapse_class_value == 'collapse':
            self.driver.execute_script("arguments[0].click()", card_heading)
            card_body = card.find_element(By.CLASS_NAME, self.accordian_card_body_class).text
        return card_heading.text, card_body

    # Date Picker Page
    def set_date(self, date):
        date_element = self.driver.find_element(By.ID, self.date_picker_id)
        date_element.clear()
        self.driver.execute_script("arguments[0].value = arguments[1];", date_element, date)

    def set_datetime(self, datetime):
        date_element = self.driver.find_element(By.ID, self.date_n_time_picker_id)
        date_element.clear()
        self.driver.execute_script("arguments[0].value = arguments[1];", date_element, datetime)

    # Range Slider page
    def set_range_slider_value(self, desired_value):
        slider = self.driver.find_element(By.XPATH, self.range_slider_input_xpath)
        display_value = self.driver.find_element(By.ID, self.range_value_display_id)
        min_value = 0
        max_value = 100

        # Set the desired values using JavaScript
        self.driver.execute_script("arguments[0].setAttribute('min', arguments[1]);", slider, min_value)
        self.driver.execute_script("arguments[0].setAttribute('max', arguments[1]);", slider, max_value)

        # Set the slider to a specific value
        self.driver.execute_script("arguments[0].value = arguments[1];", slider, desired_value)
        self.driver.execute_script("arguments[0].value = arguments[1];", display_value, desired_value)

    def set_progress_bar(self, sec):
        btn = self.driver.find_element(By.ID, self.start_stop_btn_id)
        btn.click()
        time.sleep(sec)
        btn.click()

    def get_progress_bar_value(self):
        return self.driver.find_element(By.XPATH, self.progress_bar_div).text

    # Tabs Page
    def click_tabs(self, tab_name):
        if tab_name == 'what':
            what_tab = self.driver.find_element(By.ID, self.what_tab_id)
            self.driver.execute_script("arguments[0].click()", what_tab)
        elif tab_name == 'origin':
            origin_tab = self.driver.find_element(By.ID, self.origin_tab_id)
            self.driver.execute_script("arguments[0].click()", origin_tab)
        elif tab_name == 'use':
            use_tab = self.driver.find_element(By.ID, self.use_tab_id)
            self.driver.execute_script("arguments[0].click()", use_tab)

    def get_active_tab_content(self):
        actual_content = None
        tabs_contents = self.driver.find_elements(By.CLASS_NAME, self.tab_content_div_class)
        for content in tabs_contents:
            tab_content_class = content.get_attribute('class')
            if 'active' in tab_content_class:
                actual_content = content.text
                break
        return actual_content

    def get_tool_tip_on_btn_msg(self):
        self.driver.find_element(By.ID, self.tool_tip_btn_id).click()
        tool_tip = self.driver.find_element(By.CLASS_NAME, self.btn_tool_tip_msg_div_class)
        return tool_tip.text

    def get_tool_tip_on_input_field_msg(self):
        self.driver.find_element(By.ID, self.text_field_id).click()
        tool_tip = self.driver.find_element(By.CLASS_NAME, self.btn_tool_tip_msg_div_class)
        return tool_tip.text

    def click_menu_item1(self):
        menu1 = self.driver.find_element(By.LINK_TEXT, self.menu_item1_link_text)
        href_text = menu1.get_attribute("href")
        menu1.click()
        return href_text

    def test_hover_menu(self):
        pass
        # menu2 = self.driver.find_element(By.LINK_TEXT, self.menu_item2_link_text)
        # menu2_sub_menus = self.driver.find_elements(By.LINK_TEXT, self.menu_item2_sub_item_link_text)
        # menu2_sub_menu3 = self.driver.find_element(By.LINK_TEXT, self.menu_item2_sub_item_list_link_text)
        # menu2_sub_menu3_sub1 = self.driver.find_element(By.LINK_TEXT, self.menu_item2_sub_item_list1_link_text)
        # menu2_sub_menu3_sub2 = self.driver.find_element(By.LINK_TEXT, self.menu_item2_sub_item_list2_link_text)
        # self.act.move_to_element(menu2).move_to_element(menu2_sub_menu3).move_to_element(menu2_sub_menu3_sub1).click().perform()
        # # self.driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('mouseover', {bubbles: true}));",
        # #                       menu2)

    # Select Menu Page
    def select_value_dropdown(self):
        dropdown_buttons = self.driver.find_elements(By.XPATH, self.dropdown_list_btn_xpath)
        dropdown_buttons[0].click()
        group1_option2_element = self.driver.find_element(By.ID, self.group1_option2_id)
        text = group1_option2_element.text
        group1_option2_element.click()
        return text

    def old_style_menu_style(self, color):
        old_style_dropdown_element = self.driver.find_element(By.ID, self.old_style_select_dropdown_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", old_style_dropdown_element)
        dropdown = Select(old_style_dropdown_element)
        dropdown.select_by_visible_text(color)
        return dropdown.first_selected_option.text

    def multiselect_dropdown(self):
        multiselect = self.driver.find_elements(By.XPATH, "//*[@class=' css-tlfecz-indicatorContainer']")
        self.driver.execute_script("arguments[0].scrollIntoView();", multiselect[-1])
        multiselect[-1].click()
        self.driver.find_element(By.ID, self.red_color_multi_select_id).click()
        self.driver.find_element(By.ID, self.black_color_multi_select_id).click()
        self.driver.find_element(By.ID, self.blue_color_multi_select_id).click()
        self.driver.find_element(By.ID, self.green_color_multi_select_id).click()

    def standard_multiselect(self):
        std_multi = self.driver.find_element(By.ID, "cars")
        select = Select(std_multi)
        select.select_by_visible_text("Volvo")
        select.select_by_value("saab")
        select.select_by_index(2)
        selected_list = select.all_selected_options
        return [x.text for x in selected_list]
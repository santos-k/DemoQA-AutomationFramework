# DemoQA.com Automation with Python and Selenium

This project aims to automate testing for the [DemoQA](https://demoqa.com/) website using Python and Selenium. DemoQA is a demo website used for practicing web automation skills. The project will focus on automating tests for various functionalities provided by DemoQA, including interacting with elements, filling forms, handling alerts, frames, windows, widgets, interactions, and testing the book store application.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Test Suites](#test-suites)
    - [1. Home Page Automation](#1-home-page-automation)
    - [2. Elements Page](#2-elements-page)
    - [3. Forms Page](#3-forms-page)
    - [4. Alerts, Frame & Windows Page](#4-alerts-frame--windows-page)
    - [5. Widgets Page](#5-widgets-page)
    - [6. Interactions Page](#6-interactions-page)
    - [7. Book Store Application](#7-book-store-application)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The DemoQA website provides various features and functionalities to practice web automation techniques. This project utilizes Python with Selenium to automate the testing process for DemoQA. The tests are organized into different test suites covering different sections of the website.

## Project Structure
The project follows a structured approach to organize the test code, page objects, utilities, and test cases. The project structure is as follows:
```commandline
demoqa_automation/
│
├── pageObjects/
│   ├── __init__.py
│   ├── homepage.py
│   ├── elements_page.py
│   ├── forms_page.py
│   ├── alerts_frames_windows_page.py
│   ├── widgets_page.py
│   ├── interactions_page.py
│   └── book_store_application.py
│
├── testCases/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_homepage.py
│   ├── test_elements_page.py
│   ├── test_forms_page.py
│   ├── test_alerts_frames_windows_page.py
│   ├── test_widgets_page.py
│   ├── test_interactions_page.py
│   └── test_book_store_application.py
│
├── utilities/
│   ├── __init__.py
│   ├── utils_functions.py
│   └── generate_log.py
│
├── Screenshots/
│
├── Logs/
│
├── README.md 
│
└── requirements.txt
```


Explanation:

- `conftest.py`: Fixture setup and teardown for tests.
- `pageObjects/`: Directory containing page objects for different pages of the website.
- `testCases/`: Directory containing test cases organized by test suites.
- `utilities/`: Directory containing utility functions for logging, screenshot capturing, etc.
- `Screenshots/`: Directory to store screenshots captured during tests.
- `Logs/`: Directory to store log files generated during test execution.
- `README.md`: Readme file containing project information, setup instructions, and usage guidelines.
- `requirements.txt`: File containing project dependencies.
## Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Install Python (if not already installed).
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Make sure you have the appropriate web driver executable (e.g., ChromeDriver for Chrome) installed and added to your system's PATH.

## Usage

To run the tests, navigate to the project directory and execute the following command:

```bash
pytest
```

```python
# conftest.py
from selenium import webdriver
import pytest

base_url = "https://demoqa.com/"


@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(base_url)
    yield driver
    driver.quit()
```

```python
# utilities_functions.py
import logging

class GenerateLog:
    @staticmethod
    def generate_log():
        logger = logging.getLogger()
        logger.handlers.clear()
        try:
            file_handler = logging.FileHandler(filename=".//Logs//Automation.log", mode='a')
        except FileNotFoundError:
            file_handler = logging.FileHandler(filename="../Logs/Automation.log", mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

```


This command will run all the test suites defined in the project.

## Test Suites

### 1. Home Page Automation

This test suite covers automation of the home page of the DemoQA website. It includes tests for verifying page title, presence of elements, and basic functionality.
#### Web ELements on this page:
1. Header
2. Footer
3. Cards
4. Images
5. Links

**Click using JavaScript**
```python
div = divs[index].find_elements(By.TAG_NAME, 'div')[0]
self.driver.execute_script("arguments[0].click()", div)
```

### 2. Elements Page

This test suite focuses on automating tests related to the "Elements" section of the DemoQA website. It includes tests for various elements such as text boxes, check boxes, radio buttons, buttons, web tables, links, upload and download functionality, and dynamic properties.
#### Elements on this Page:
1. **Text Box**
    - using **send_keys()** method
   ```python
    self.driver.find_element(By.CSS_SELECTOR, self.username_input_css).send_keys(full_name)
    ```
   - using **execute_script()** method
   ```python
    email_element = self.driver.find_element(By.CSS_SELECTOR, self.email_input_css)
    self.driver.execute_script("arguments[0].value = arguments[1];", email_element, "abc@gmail.com")
    ```
2. **Check Box**
    ```python
    self.driver.find_element(By.CLASS_NAME, self.expand_all_checkboxes_button_class).click()
    ```
3. **Radio Button**
    ```python
    if value.lower() == "yes":
        yes_radio = self.driver.find_element(By.CSS_SELECTOR, self.yes_radio_btn_css)
        self.driver.execute_script("arguments[0].click()", yes_radio)
    elif value.lower() == "impressive":
        impressive_radio = self.driver.find_element(By.CSS_SELECTOR, self.impressive_radio_btn_css)
        self.driver.execute_script("arguments[0].click()", impressive_radio)
    elif value.lower() == 'no':
        return self.driver.find_element(By.CSS_SELECTOR, self.no_radio_btn_css).is_enabled()
    ```
4. **Web Tables**
- Get tables header/columns name
   ```python
   def get_table_columns_name(self):
       columns = self.driver.find_elements(By.XPATH, self.table_columns_xpath)
       return [column.text for column in columns]
   ```
  - Get Table rows records as dict
   ```python
   def get_table_rows_data(self):
       data = {}
       rows = self.driver.find_elements(By.CLASS_NAME, self.table_rows_data_class)
       for index, row in enumerate(rows):
           data[index] = row.text.split("\n")
       return data
   ```
5. **Buttons**
- Double Click
    ```python
    def double_click(self):
        double_btn = self.driver.find_element(By.ID, self.double_click_btn_id)
        self.act.double_click(double_btn).perform()
    ```
- Right Click also known as context click
  ```python
  def right_click(self):
      right_btn = self.driver.find_element(By.ID, self.right_click_btn_id)
      self.act.context_click(right_btn).perform()
  ```
6. **Links**
     ```python
        self.driver.find_element(By.LINK_TEXT, link_text).click()
        or 
        click_link = self.driver.find_element(By.LINK_TEXT, link_text)
        self.driver.execute_script("arguments[0].click()", click_link)
    ```
7. **Broken Images - Links**: similar as links
8. **Upload and Download**
```python
    def upload_download(self, n, file):
        if n == 'upload':
            self.driver.find_element(By.ID, self.upload_id).send_keys(file)
            return self.driver.find_element(By.ID, self.upload_file_path_id).text
        elif n == 'download':
            self.driver.find_element(By.ID, self.download_btn_id).click()
        else:
            pass
```
9. **Dynamic Properties**: like elements will appear after 5 seconds, text color change, visible for 5 seconds
    ```python
    time.sleep(5)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    ```

### 3. Forms Page

This test suite covers automation of tests related to the "Forms" section of the DemoQA website. It includes tests for interacting with the simple student registration form.
#### Elements on this page:
- Text box, check box, radio button, textarea, upload, dropdown
- **Check Boxe**:
  - Method to work with 3 check boxes, first uncheck all checked boxes ,then check as per required
    ```python
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
    ```
- **Dropdown**:
  - Method for dropdown select
      ```python
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
      ```

### 4. Alerts, Frame & Windows Page

This test suite focuses on automating tests related to the "Alerts, Frame & Windows" section of the DemoQA website. It includes tests for handling browser windows, alerts, frames, nested frames, and model dialogs.
#### Elements on this page:
1. New Tabs and windows
   - Open new tab 
    ```python
        # Switch to the new tab
        driver.switch_to.window("new_tab")
   
        # Open another tab in the new window
        driver.execute_script("window.open('https://www.example.com/page4', 'another_tab')")
    ``` 
    - Open new window
    ```python
        # Switch to the new blank window
        driver.switch_to.window("new_window")
       
        # Open a new window with url
        driver.execute_script("window.open('https://www.example.com/page3', 'new_window')")
    ```
   - Switch between windows
   ```python
   win_handles = self.driver.window_handles
   self.driver.switch_to.window(win_handles[1])
   ```
   
2. Alerts, Confirm and Prompt
   1. Alerts
      ```python    
      def test_alert(self):
        self.alertpage.click_alert_button()
        alert = self.driver.switch_to.alert
        alert.accept()
        assert "You clicked a button" == alert.text```
   2. Confirm
   ```python
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
   ```
   3. Prompt
   ```python
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
   ```
3. Frames
    ```python
        def test_large_frame(self):
            self.driver.switch_to.frame(self.alertpage.large_frame_id)
            text = self.alertpage.get_large_frame_content()
            assert text == "This is a sample page"
    ```
4. Nested Frames
    ```python
        def test_parent_frame(self):
            self.driver.switch_to.frame(self.alertpage.parent_frame_id)
            content = self.alertpage.get_parent_frame_content()
            assert "Parent frame" == content
    
            self.driver.switch_to.frame(0)
            content = self.alertpage.get_parent_frame_content()
            assert "Child Iframe" == content
    ```
5. Modal Dialogs
```python
    def test_small_model(self):
        self.alertpage.get_small_model()
        title = self.alertpage.get_model_title()
        body = self.alertpage.get_model_body_text()
        assert "Small Modal" in title
        assert "small modal" in body
        self.alertpage.close_model_by_btn('s')
```

### 5. Widgets Page

This test suite covers automation of tests related to the "Widgets" section of the DemoQA website. It includes tests for various widgets such as accordion, auto complete, date picker, slider, progress bar, tabs, tool tips, menu, and select menu.
Elements on this page:
1. **Accordian**
```python
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
```
1. **Auto Complete**
1. **Date Picker**
```python
    def set_date(self, date):
        date_element = self.driver.find_element(By.ID, self.date_picker_id)
        date_element.clear()
        self.driver.execute_script("arguments[0].value = arguments[1];", date_element, date)

    def set_datetime(self, datetime):
        date_element = self.driver.find_element(By.ID, self.date_n_time_picker_id)
        date_element.clear()
        self.driver.execute_script("arguments[0].value = arguments[1];", date_element, datetime)
```
1. **Slider**
```python
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

```
1. **Progress Bar**
```python
    def set_progress_bar(self, sec):
        btn = self.driver.find_element(By.ID, self.start_stop_btn_id)
        btn.click()
        time.sleep(sec)
        btn.click()

    def get_progress_bar_value(self):
        return self.driver.find_element(By.XPATH, self.progress_bar_div).text

```
1. **Tabs**
```python
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
```
1. **Tool Tips**
```python
    def get_tool_tip_on_btn_msg(self):
        self.driver.find_element(By.ID, self.tool_tip_btn_id).click()
        tool_tip = self.driver.find_element(By.CLASS_NAME, self.btn_tool_tip_msg_div_class)
        return tool_tip.text

    def get_tool_tip_on_input_field_msg(self):
        self.driver.find_element(By.ID, self.text_field_id).click()
        tool_tip = self.driver.find_element(By.CLASS_NAME, self.btn_tool_tip_msg_div_class)
        return tool_tip.text
```
1. **Menu**
```python
    def click_menu_item1(self):
        menu1 = self.driver.find_element(By.LINK_TEXT, self.menu_item1_link_text)
        href_text = menu1.get_attribute("href")
        menu1.click()
        return href_text
```
1. **Select Menu**
```python
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
```


### 6. Interactions Page

This test suite focuses on automating tests related to the "Interactions" section of the DemoQA website. It includes tests for sortable, selectable, resizable, droppable, and draggable interactions.
#### Elements on this Page:
 1. **Sortable**
```python
# List Shortable
list_items_container = self.driver.find_element(By.CSS_SELECTOR, self.div_of_lists_css)
list_items = list_items_container.find_elements(By.CSS_SELECTOR, self.list_divs_css)
for i in range(3):
    self.act.drag_and_drop(list_items[i], list_items[-1]).perform()

# Grid Shortable
grid_items_container = self.driver.find_element(By.CLASS_NAME, self.grid_class)
grid_items = grid_items_container.find_elements(By.TAG_NAME, 'div')

self.act.drag_and_drop(grid_items[-1], grid_items[0]).perform()
self.act.drag_and_drop(grid_items[-2], grid_items[1]).perform()
self.act.drag_and_drop(grid_items[-3], grid_items[2]).perform()

```
2. **Selectable**
```python
# List items selectable
list_items_container = self.driver.find_element(By.ID, self.selectable_lists_ul_id)
list_items = list_items_container.find_elements(By.TAG_NAME, 'li')
for i in list_items:
    i.click()

# Grid items selectable
grid_items = self.driver.find_elements(By.XPATH, self.selectable_grid_items_xpath)
for i in range(0, 9, 2):
    grid_items[i].click()
```
3. **Resizable**
```python
    def resize_small_div(self, width, height):
        small_div_element = self.driver.find_element(By.ID, self.small_div_inside_large_div_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", small_div_element)
        self.driver.execute_script(f"arguments[0].style.width = '{width}px';", small_div_element)
        self.driver.execute_script(f"arguments[0].style.height = '{height}px';", small_div_element)
        return small_div_element.size['width'], small_div_element.size['height']

    def resizable_div(self, width, height):
        resizeable_div_element = self.driver.find_element(By.ID, self.resizable_large_div_id)
        self.driver.execute_script("arguments[0].scrollIntoView();", resizeable_div_element)
        self.driver.execute_script(f"arguments[0].style.width = '{width}px';", resizeable_div_element)
        self.driver.execute_script(f"arguments[0].style.height = '{height}px';", resizeable_div_element)
        return resizeable_div_element.size['width'], resizeable_div_element.size['height']
```
4. **Droppable**
```python
# simple drop
self.act.drag_and_drop(source_element, target_element).perform()
```
5. **Draggable**
```python
# drag with position
self.act.drag_and_drop_by_offset(child, 20, 20)
```


### 7. Book Store Application

This test suite covers automation of tests related to the "Book Store Application" section of the DemoQA website. It includes tests for login, browsing books, managing profile, and interacting with the book store API.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve the project.

## License

This project is licensed under the [MIT License](LICENSE).

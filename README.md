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

### 2. Elements Page

This test suite focuses on automating tests related to the "Elements" section of the DemoQA website. It includes tests for various elements such as text boxes, check boxes, radio buttons, buttons, web tables, links, upload and download functionality, and dynamic properties.

### 3. Forms Page

This test suite covers automation of tests related to the "Forms" section of the DemoQA website. It includes tests for interacting with the simple student registration form.

### 4. Alerts, Frame & Windows Page

This test suite focuses on automating tests related to the "Alerts, Frame & Windows" section of the DemoQA website. It includes tests for handling browser windows, alerts, frames, nested frames, and model dialogs.

### 5. Widgets Page

This test suite covers automation of tests related to the "Widgets" section of the DemoQA website. It includes tests for various widgets such as accordion, auto complete, date picker, slider, progress bar, tabs, tool tips, menu, and select menu.

### 6. Interactions Page

This test suite focuses on automating tests related to the "Interactions" section of the DemoQA website. It includes tests for sortable, selectable, resizable, droppable, and draggable interactions.

### 7. Book Store Application

This test suite covers automation of tests related to the "Book Store Application" section of the DemoQA website. It includes tests for login, browsing books, managing profile, and interacting with the book store API.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve the project.

## License

This project is licensed under the [MIT License](LICENSE).

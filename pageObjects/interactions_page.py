import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Interactions_Page:
    # Shortable elements
    tab_list_id = "demo-tab-list"
    tab_grid_id = "demo-tab-grid"
    div_of_lists_css = "div[class='vertical-list-container mt-4']"
    list_divs_css = "div[class='list-group-item list-group-item-action']"
    grid_class = "create-grid"

    # Selectable elements
    selectable_lists_ul_id = "verticalListContainer"
    selectable_grid_items_xpath = "//*[@id='gridContainer']//li"

    # Resizeable page
    large_div_class = "constraint-area"
    small_div_inside_large_div_id = "resizableBoxWithRestriction"
    text_div_inside_small_div_xpath = "//*[@id='resizableBoxWithRestriction']//div"
    resizable_large_div_id = "resizable"

    # Droppable page
    simple_tab_id = "droppableExample-tab-simple"
    drag_me_item_id = "draggable"
    drop_here_div_id = "droppable"

    accept_tab_id = "droppableExample-tab-accept"
    acceptable_div_id = "acceptable"
    not_acceptable_div_id = "notAcceptable"

    prevent_propagation_tab_id = "droppableExample-tab-preventPropogation"
    drag_me_div_id = "dragBox"
    not_greedy_outer_div_id = "notGreedyDropBox"
    not_greedy_inner_div_id = "notGreedyInnerDropBox"

    revert_draggable_tab_id = "droppableExample-tab-revertable"
    will_revert_css = "#revertable"
    will_not_revert_css = "#notRevertable"

    # Draggable Page
    simple_drag_tab_css = "#draggableExample-tab-simple"
    drag_me_id = "dragBox"

    axis_restricted_tab_css = "#draggableExample-tab-axisRestriction"
    only_x_allowed_id = "restrictedX"
    only_y_allowed_id = "restrictedY"

    container_restricted_tab_css = "#draggableExample-tab-containerRestriction"
    container_div_id = "containmentWrapper"

    cursor_style_tab_css = "#draggableExample-tab-cursorStyle"
    cursor_center_id = "cursorCenter"
    cursor_topLeft_id = "cursorTopLeft"
    cursor_bottom_id = "cursorBottom"

    def __init__(self, driver):
        self.driver = driver
        self.act = ActionChains(self.driver)

    def sortable_lists(self):
        list_tab_element = self.driver.find_element(By.ID, self.tab_list_id)
        list_tab_element.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", list_tab_element)

        list_items_container = self.driver.find_element(By.CSS_SELECTOR, self.div_of_lists_css)
        list_items = list_items_container.find_elements(By.CSS_SELECTOR, self.list_divs_css)
        for i in range(3):
            self.act.drag_and_drop(list_items[i], list_items[-1]).perform()
        return ['Two', 'Four', 'Six', 'One', 'Three', 'Five']

    def sortable_grid(self):
        grid_tab_element = self.driver.find_element(By.ID, self.tab_grid_id)
        grid_tab_element.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", grid_tab_element)

        grid_items_container = self.driver.find_element(By.CLASS_NAME, self.grid_class)
        grid_items = grid_items_container.find_elements(By.TAG_NAME, 'div')

        self.act.drag_and_drop(grid_items[-1], grid_items[0]).perform()
        self.act.drag_and_drop(grid_items[-2], grid_items[1]).perform()
        self.act.drag_and_drop(grid_items[-3], grid_items[2]).perform()
        assert [x.text for x in grid_items]

    # Selectable
    def selectable_list_items(self):
        list_tab_element = self.driver.find_element(By.ID, self.tab_list_id)
        list_tab_element.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", list_tab_element)

        list_items_container = self.driver.find_element(By.ID, self.selectable_lists_ul_id)
        list_items = list_items_container.find_elements(By.TAG_NAME, 'li')
        for i in list_items:
            i.click()
        return [x.text for x in list_items]

    def selectable_grid_items(self):
        grid_tab_element = self.driver.find_element(By.ID, self.tab_grid_id)
        grid_tab_element.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", grid_tab_element)

        grid_items = self.driver.find_elements(By.XPATH, self.selectable_grid_items_xpath)
        for i in range(0, 9, 2):
            grid_items[i].click()

        time.sleep(2)
        for i in range(0, 9, 2):
            grid_items[i].click()

        for i in range(1, 9, 2):
            grid_items[i].click()
        time.sleep(2)
        return [x.text for x in grid_items]

    # Resizable
    def resize_small_div_vertically(self, width, height):
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

    # Droppable
    def simple_drag_drop(self):
        tab = self.driver.find_element(By.ID, self.simple_tab_id)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        source_element = self.driver.find_element(By.ID, self.drag_me_item_id)
        target_element = self.driver.find_element(By.ID, self.drop_here_div_id)
        time.sleep(1)
        self.act.drag_and_drop(source_element, target_element).perform()
        return target_element.text

    def acceptable_drag_into_drop(self, accept=True):
        tab = self.driver.find_element(By.ID, self.accept_tab_id)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        acceptable_source_element = self.driver.find_element(By.ID, self.acceptable_div_id)
        not_acceptable_source_element = self.driver.find_element(By.ID, self.not_acceptable_div_id)
        target_element = self.driver.find_elements(By.XPATH, "//div[@id='droppable']")[1]
        time.sleep(1)
        if not accept:
            self.act.drag_and_drop(not_acceptable_source_element, target_element).perform()
            return target_element.text
        else:
            self.act.drag_and_drop(acceptable_source_element, target_element).perform()
            return target_element.text

    def prevent_propagation_drag_drop(self):
        tab = self.driver.find_element(By.ID, self.prevent_propagation_tab_id)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        drag_this = self.driver.find_element(By.ID, self.drag_me_div_id)
        drop_here_inner = self.driver.find_element(By.ID, self.not_greedy_inner_div_id)
        time.sleep(1)
        self.act.drag_and_drop(drag_this, drop_here_inner).perform()
        return drop_here_inner.text

    def revert_able_drag(self, revert=True):
        tab = self.driver.find_element(By.ID, self.revert_draggable_tab_id)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        will_revert_div = self.driver.find_element(By.CSS_SELECTOR, self.will_revert_css)
        will_revert_position = will_revert_div.location
        x_pos, y_pos = will_revert_position['x'], will_revert_position['y']
        will_not_revert_div = self.driver.find_element(By.CSS_SELECTOR, self.will_not_revert_css)
        will_not_revert_position = will_not_revert_div.location
        x_pos_n, y_pos_n = will_not_revert_position['x'], will_not_revert_position['y']
        target_element = self.driver.find_elements(By.ID, self.drop_here_div_id)[2]
        time.sleep(1)
        if not revert:
            self.act.drag_and_drop(will_not_revert_div, target_element).perform()
            time.sleep(1)
            will_not_revert_position = will_not_revert_div.location
            x_pos2, y_pos2 = will_not_revert_position['x'], will_not_revert_position['y']
            x = x_pos != x_pos2
            y = y_pos != y_pos2
            return x == y, target_element.text
        else:
            self.act.drag_and_drop(will_not_revert_div, target_element).perform()
            time.sleep(1)
            will_revert_position = will_not_revert_div.location
            x_pos_n2, y_pos_n2 = will_revert_position['x'], will_revert_position['y']
            x = x_pos_n == x_pos_n2
            y = y_pos_n == y_pos_n2
            return x == y, target_element.text

    # Draggable page
    def simple_draggable(self):
        tab = self.driver.find_element(By.CSS_SELECTOR, self.simple_drag_tab_css)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        drag_me = self.driver.find_element(By.ID, self.drag_me_id)
        time.sleep(1)
        self.act.drag_and_drop_by_offset(drag_me, 200, 100).perform()
        time.sleep(1)

    def y_axis_restricted(self, x_pos=50):
        tab = self.driver.find_element(By.CSS_SELECTOR, self.axis_restricted_tab_css)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        only_x = self.driver.find_element(By.ID, self.only_x_allowed_id)
        self.act.drag_and_drop_by_offset(only_x, x_pos, 0).perform()

    def x_axis_restricted(self, y_pos=50):
        tab = self.driver.find_element(By.CSS_SELECTOR, self.axis_restricted_tab_css)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        only_x = self.driver.find_element(By.ID, self.only_y_allowed_id)
        self.act.drag_and_drop_by_offset(only_x, 0, y_pos).perform()

    def container_restricted(self, x, y):
        tab = self.driver.find_element(By.CSS_SELECTOR, self.container_restricted_tab_css)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)

        parent_container = self.driver.find_element(By.ID, self.container_div_id)
        child_container = parent_container.find_element(By.TAG_NAME, 'div')
        time.sleep(4)
        self.act.drag_and_drop_by_offset(child_container, x, y).perform()
        time.sleep(4)

    def container_restricted_text(self):
        tab = self.driver.find_element(By.CSS_SELECTOR, self.container_restricted_tab_css)
        tab.click()

        parent = self.driver.find_elements(By.CSS_SELECTOR, "div.draggable")[-1]
        child = parent.find_element(By.TAG_NAME, 'span')
        self.driver.execute_script("arguments[0].scrollIntoView();", child)

        time.sleep(3)
        self.act.drag_and_drop_by_offset(child, 20, 20)
        time.sleep(3)

    # Cursor Style
    def cursor_style_position(self):
        tab = self.driver.find_element(By.CSS_SELECTOR, self.cursor_style_tab_css)
        tab.click()
        self.driver.execute_script("arguments[0].scrollIntoView();", tab)
        top_cursor = self.driver.find_element(By.ID, self.cursor_topLeft_id)
        center_cursor = self.driver.find_element(By.ID, self.cursor_center_id)
        bottom_cursor = self.driver.find_element(By.ID, self.cursor_bottom_id)

        time.sleep(2)
        self.act.drag_and_drop_by_offset(top_cursor, 100, 0)
        time.sleep(2)
        self.act.drag_and_drop_by_offset(center_cursor, 60, 20)
        time.sleep(2)
        self.act.drag_and_drop_by_offset(bottom_cursor, 20, 100)
        time.sleep(2)

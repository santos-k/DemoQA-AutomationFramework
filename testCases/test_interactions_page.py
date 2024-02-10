import pytest
from pageObjects.elements_page import Element_Page
from pageObjects.homepage import Homepage
from pageObjects.interactions_page import Interactions_Page


class Test_ShortableListGrids:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elements_page = Element_Page(self.driver)
        self.elements_page.open_sub_menus(4, 0)
        self.interactions = Interactions_Page(self.driver)

    def test_sortable_list(self):
        shorted_list = self.interactions.sortable_lists()
        assert shorted_list == ['Two', 'Four', 'Six', 'One', 'Three', 'Five']

    def test_sortable_grid(self):
        self.interactions.sortable_grid()
        assert True


class Test_SelectableListGrids:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elements_page = Element_Page(self.driver)
        self.elements_page.open_sub_menus(4, 1)
        self.interactions = Interactions_Page(self.driver)

    def test_select_list(self):
        list_items = self.interactions.selectable_list_items()
        assert 'Dapibus ac facilisis in' in list_items

    def test_select_grid(self):
        grid_items_text = self.interactions.selectable_grid_items()
        assert 'One' in grid_items_text


class Test_ResizeableBox:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elements_page = Element_Page(self.driver)
        self.elements_page.open_sub_menus(4, 2)
        self.interactions = Interactions_Page(self.driver)

    @pytest.mark.parametrize(('width, height'), [(150, 150), (200, 200), (500, 300)])
    def test_resizeable_inner_box(self, height, width):
        actual_width, actual_height = self.interactions.resize_small_div_vertically(width, height)
        assert actual_width == width
        assert actual_height == height

    @pytest.mark.parametrize(('width, height'), [(350, 450), (600, 200)])
    def test_resizeable_outer_box(self, width, height):
        actual_width, actual_height = self.interactions.resizeable_div(width, height)
        assert actual_width == width
        assert actual_height == height


class Test_Droppable:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elements_page = Element_Page(self.driver)
        self.elements_page.open_sub_menus(4, 3)
        self.interactions = Interactions_Page(self.driver)

    def test_simple_droppable(self):
        text = self.interactions.simple_drag_drop()
        assert text == 'Dropped!', 'Not matched'

    @pytest.mark.parametrize(('accept, result'), [(True, 'Dropped!'), (False, 'Drop here')])
    def test_acceptable_drop(self, accept, result):
        text = self.interactions.acceptable_drag_into_drop(accept=accept)
        assert result == text, 'Not matched'

    def test_prevent_propagation(self):
        text = self.interactions.prevent_propagation_drag_drop()
        assert text == 'Dropped!'

    @pytest.mark.parametrize(('revert'), [(True), (False)])
    def test_revert_draggable(self, revert):
        status, text = self.interactions.revert_able_drag(revert)
        assert status
        assert text == 'Dropped!'


class Test_Draggable:
    @pytest.fixture(autouse=True)
    def init_setup(self, setup):
        self.driver = setup
        self.homepage = Homepage(self.driver)
        self.homepage.click_alertFrameWindow()
        self.elements_page = Element_Page(self.driver)
        self.elements_page.open_sub_menus(4, 4)
        self.interactions = Interactions_Page(self.driver)

    def test_simple_draggable(self):
        self.interactions.simple_draggable()
        assert True

    def test_y_axis_restricted(self):
        self.interactions.y_axis_restricted(x_pos=100)
        assert True

    def test_x_axis_restricted(self):
        self.interactions.x_axis_restricted(y_pos=80)
        assert True

    def test_container_restricted(self):
        self.interactions.container_restricted(70, 50)

    def test_container_restricted_text(self):
        self.interactions.container_restricted_text()

    def test_cursor_style(self):
        self.interactions.cursor_style_position()

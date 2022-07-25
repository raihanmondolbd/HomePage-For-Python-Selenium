from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException, \
    WebDriverException
import time


# this Base class is serving basic attributes for every single page inherited from Page class
class BasePage(object):
    def __init__(self, driver, base_url="about:blank"):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 90

    def send_keys_without_selecting_element(self, text=""):
        """
        Sends keys to the focused input field without selecting the element.
        Sends keys to field where cursor is present.
        :param text: str
        :return: None
        """
        actions = ActionChains(self.driver)
        actions.send_keys(text)
        actions.perform()

    # right Click
    def rightClick(self, *locator):
        element = self.find_element(*locator)
        rightclick = ActionChains(self.driver).move_to_element(element)
        rightclick.context_click().perform()

    # Get text of multiple elements
    def get_text_of_multiple_element(self, *locator):
        elements = self.find_elements(*locator)
        val = []
        for element in elements:
            val.append(element.text)
        return val

    # Find single element
    def find_element2(self, *locator):
        return self.driver.find_element(*locator)

    def find_element(self, *locator):
        return self.wait_till_visibility_of_element_located(30, *locator)

    # Find multiple elements
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    # Mouse hover on an element
    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # change iframe
    def change_frame(self, locator):
        self.driver.switch_to.frame(locator)

    # change to default frame
    def change_to_default_frame(self):
        self.driver.switch_to.default_content()

    # Element is displayed or not
    def element_is_displayed(self, *locator):
        element = self.find_element(*locator)
        res = element.is_displayed()
        return res

    # Element is clickable or not
    def element_is_clickable(self, *locator):
        element = self.find_element(*locator)
        try:
            element.click()
            res = True
        except WebDriverException:
            res = False
        return res

    # Get attribute
    def get_attribute_value(self, attribute, *locator):
        element = self.driver.find_element(*locator)
        val = element.get_attribute(attribute)
        # print(val)
        return val

    # select all the word from text content

    def select_all(self, *locator):
        try:
            action = ActionChains(self.driver)
            action.key_down(Keys.CONTROL).send_keys('A').perform()
        except Exception as e:
            print(e)
            self.driver.find_element(*locator).send_keys(Keys.CONTROL, "a")

    def copy_all_selected(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL, "c")

    def switch_to_first_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def paste_all_selected(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL, "p")

    def save_shortcut(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys('S').perform()

    def press_space_bar(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.SPACE)

    def cut_all_selected(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL, "x")

    def press_cntrl_z(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "z")

    def press_cntrl_y(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "y")

    def save_shortcut_with_locator(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "s")

    def press_Cntrl_A(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "a")

    def press_Cntrl_I(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "i")

    def press_Cntrl_U(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "u")

    def press_Cntrl_B(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "b")

    def press_Cntrl_V(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "v")

    def press_Cntrl_X(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + "x")

    def press_space_dot(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.SPACE + ".")

    def Press_Cntrl_And_Enter(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.CONTROL + Keys.ENTER)

    def click_backspace_with_locator(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.BACKSPACE)

    def go_to_left_using_left_arrow_key(self, times, *locator):
        for i in range(times):
            self.driver.find_element(*locator).send_keys(Keys.CONTROL + Keys.ARROW_LEFT)

    def go_to_right_using_right_arrow_key(self, times, *locator):
        for i in range(times):
            self.driver.find_element(*locator).send_keys(Keys.CONTROL + Keys.ARROW_RIGHT)

    def go_to_up_using_up_arrow_key(self, times, *locator):
        for i in range(times):
            self.driver.find_element(*locator).send_keys(Keys.CONTROL + Keys.ARROW_UP)

    def go_to_down_using_down_arrow_key(self, times, *locator):
        for i in range(times):
            self.driver.find_element(*locator).send_keys(Keys.CONTROL + Keys.ARROW_DOWN)

    # Get multiple attribute
    def get_multiple_attribute_value(self, attributes, *locator):
        element = self.driver.find_element(*locator)
        val = []
        for attribute in attributes:
            val.append(element.get_attribute(attribute))
        return val

    # Get CSS property
    def get_css_property(self, attribute, *locator):
        element = self.find_element(*locator)
        val = element.value_of_css_property(attribute)
        # print(val)
        return val

    # Get text
    def get_text(self, *locator):
        element = self.find_element(*locator)
        val = element.text
        # print(val)
        return val

    # Get element tag
    def get_element_tag(self, *locator):
        element = self.find_element(*locator)
        val = element.tag_name
        # print(val)
        return val

    # drag and drop functions
    def drag_and_drop(self, source_locator, target_locator):
        print(source_locator, target_locator)
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop = ActionChains(self.driver).drag_and_drop(source, target)
        drag_and_drop.perform()

    def open_new_tab_on_browser(self, url):
        self.driver.execute_script(f'''window.open("{url}", "_blank");''')

    # Drag and drop by offset
    def drag_and_drop_offset(self, xoffset, yoffset, *source_locator):
        source = self.driver.find_element(*source_locator)
        drag_and_drop = ActionChains(self.driver).drag_and_drop_by_offset(source, xoffset, yoffset)
        drag_and_drop.perform()

    # Send data
    def send_data(self, data, *locator):
        element = self.find_element(*locator)
        element.send_keys(data)

    # Clear input field
    def clear_input_field(self, *locator):
        element = self.find_element(*locator)
        element.send_keys(Keys.CONTROL + 'a')
        element.send_keys(Keys.DELETE)

    # Clear input field and then send data to input field
    def clear_field_and_send_keys(self, data, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(data)

    # Clear input field and then send data to input field
    def clear_field(self, *locator):
        element = self.find_element(*locator)
        element.clear()

    # Get num of dropdown element
    def get_num_of_dropdown_element(self, *locator):
        select = Select(self.find_element(*locator))
        options = select.options
        return len(options)

    # Get list of dropdown element
    def get_list_of_dropdown_element(self, *locator):
        select = Select(self.find_element(*locator))
        options = select.options
        option_values = []
        for option in options:
            option_values.append(option.text)
        return option_values

    # Get active option in select
    def get_active_option_of_dropdown_element(self, *locator):
        select = Select(self.driver.find_element(*locator))
        selected_option_text = select.first_selected_option.text
        return selected_option_text

    def get_active_option_value_of_dropdown_element(self, *locator):
        select = Select(self.driver.find_element(*locator))
        selected_option_value = select.first_selected_option.get_attribute('value')
        return selected_option_value

    # Select dropdown elements
    def select_dropdown_element(self, name, *locator):
        select = Select(self.find_element(*locator))
        options = select.options
        option_values = []
        for option in options:
            option_values.append(option.text)
        # print(option_values)
        select.select_by_index(option_values.index(name))

    # Select 'Select' element by index value
    def select_by_index(self, index, *locator):
        select = Select(self.find_element(*locator))
        return select.select_by_index(index)

    # Select 'Select' element by visible text
    def select_by_visible_text(self, text, *locator):
        select = Select(self.find_element(*locator))
        return select.select_by_visible_text(text)

    # Select 'Select' element by value
    def select_by_value(self, value, *locator):
        select = Select(self.find_element(*locator))
        return select.select_by_value(value)

    # This function will scroll down to the bottom
    def goto_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # Get list of all options
    def get_all_options(self, *locator):
        select = Select(self.find_element(*locator))
        options = select.options
        return options

    # Click
    def click(self, *locator):
        element = self.find_element(*locator)
        element.click()

    @staticmethod
    def click_web_element(self, element):
        element.click()

    # move cursor to element
    def move_cursor_to_element(self, *locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    def move_cursor_to_web_element(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

    #  wait till presence of element is located
    def wait_till_presence_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.presence_of_element_located(*locator))
        return element

    #  wait till visibility_of_element_located
    def wait_till_visibility_of_element_located(self, seconds, *locator):
        try:
            ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
            wait = WebDriverWait(self.driver, seconds, ignored_exceptions=ignored_exceptions)
            element = wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException:
            print(f"\n locator {locator}  NOT FOUND WITHIN GIVEN TIME! --> {seconds}")

    #  wait till invisibility_of_element_located
    def wait_till_invisibility_of_element_located(self, seconds, *locator):
        wait = WebDriverWait(self.driver, seconds)
        element = wait.until(ec.invisibility_of_element_located(locator))
        # print(element)
        return element

    # Implicit wait
    def implicit_waits(self, seconds):
        return self.driver.implicitly_wait(seconds)

    # Press key
    def press_enter(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def press_arrow_up(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.ARROW_UP)

    def press_arrow_down(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.ARROW_DOWN)

    def press_arrow_left(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.ARROW_LEFT)

    def press_space(self, *locator):
        self.driver.find_element(*locator).send_keys(Keys.SPACE)

    # Open url
    def open_url(self, url):
        self.driver.get(url)

    def current_url(self):
        return self.driver.current_url

    # Open new tab
    def open_new_tab(self):
        self.driver.execute_script("window.open('');")
        self.switch_to_window_by_handle_number(-1)

    # Open url on new tab
    def open_url_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}','_blank')")
        self.switch_to_window_by_handle_number(-1)

    # Open url on new window opening in new tab not window
    def open_url_new_window(self, url):
        self.driver.execute_script(f"window.open('{url}','new_window')")
        self.switch_to_window_by_handle_number(-1)

    # Switch tab
    def switch_tab(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

    # Switch to window by window(e.g. CDwindow-BD9C79EE569362CD463868B54C725BEF [get by current window handle] )
    def switch_to_window_by_window(self, window):
        return self.driver.switch_to.window(window)

    # Switch to window by window handle number
    def switch_to_window_by_handle_number(self, handle_number):
        return self.driver.switch_to.window(self.driver.window_handles[handle_number])

    # Switch to parent window
    def switch_to_parent_window(self):
        return self.driver.switch_to.default_content()

    # Get current window handle
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    # Get list of all window handles
    def get_all_window_handles(self):
        return self.driver.window_handles

    # Get length of all window handles
    def get_number_of_all_window_handles(self):
        handles = self.driver.window_handles
        return len(handles)

    # Refresh page
    def refresh(self):
        return self.driver.refresh()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0,0)")

    # Assertions
    def assert_element_is_displayed(self, message="element is found", *locator):
        res = self.element_is_displayed(*locator)
        # print(res)
        assert res is True
        print(message)

    def assert_element_is_not_displayed(self, *locator):
        # print(locator)
        message = "element is not found"
        try:
            element = self.driver.find_element(*locator)
            res = element.is_displayed()
            # print('>>>', res)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as e:
            # except WebDriverException:
            #     print(WebDriverException)
            # print(e)
            res = False
            # print('<<<', res)
        # print(res)
        assert res is False
        print(message)

    def assert_element_is_clickable(self, choice, message, *locator):
        res = self.element_is_clickable(*locator)
        # print(res)
        if choice is True:
            assert res is True
        else:
            assert res is False
        print(message)

    def assert_css_property_value(self, choice, attribute, expected_val, *locator):
        val = self.get_css_property(attribute, *locator)
        # print(val)
        if val.startswith('rgba'):
            val = self.rgba_to_hex(val)
            # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    def assert_css_property_value_web_element(self, choice, attribute, expected_val, element):
        val = element.value_of_css_property(attribute)
        # print(val)
        # print(val)
        if val.startswith('rgba'):
            val = self.rgba_to_hex(val)
            # print(val)
        if val.startswith('rgb'):
            val = self.rgb_to_hex(val)
            # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    def assert_element_attribute_value(self, choice, attribute, expected_val, *locator):
        val = self.get_attribute_value(attribute, *locator)
        # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    def assert_element_attribute_value_in(self, choice, attribute, expected_val, *locator):
        val = self.get_attribute_value(attribute, *locator)
        # print(val)
        if choice == 'In':
            assert val in expected_val
        else:
            assert val not in expected_val

    def assert_element_attribute_expected_in_value(self, choice, attribute, expected_val, *locator):
        val = self.get_attribute_value(attribute, *locator)
        # print(val, expected_val)
        if choice == 'In':
            assert expected_val in val
        else:
            assert expected_val not in val

    @staticmethod
    def assert_element_attribute_expected_in_value_web_element(choice, attribute, expected_val, web_element):
        val = web_element.get_attribute(attribute)
        print(val, expected_val)
        if choice == 'In':
            assert expected_val in val
        else:
            assert expected_val not in val

    def assert_element_text(self, choice, expected_val, *locator):
        val = self.get_text(*locator)
        # print(val)
        if choice is True:
            assert val == expected_val
        else:
            # print('>>>>>>>>>>>>>>>', val)
            assert val != expected_val

    def assert_element_text_in(self, choice, expected_val, *locator):
        val = self.get_text(*locator)
        # print(val)
        if choice == 'In':
            assert expected_val in val
        else:
            assert expected_val not in val

    def assert_element_tag(self, choice, expected_val, *locator):
        val = self.get_element_tag(*locator)
        # print(val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    def assert_active_option_of_dropdown_element(self, choice, expected_val, *locator):
        val = self.get_active_option_of_dropdown_element(*locator)
        # print(val, expected_val)
        if choice is True:
            assert val == expected_val
        else:
            assert val != expected_val

    def assert_blank_checkbox_element(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result

    def assert_checkbox_element(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result

    # assert element has attribute or not. For present: result = 'true' and not_present: result = None
    def assert_is_attribute_present(self, attribute, result, *locator):
        val = self.get_attribute_value(attribute, *locator)
        assert val == result

    # CSS related function
    @staticmethod
    def rgba_to_hex(rgba):
        rgba = eval(rgba.split('a')[-1])
        return '#{:02x}{:02x}{:02x}'.format(*rgba)

    @staticmethod
    def rgb_to_hex(rgb):
        rgb = eval(rgb.split('b')[-1])
        return '#{:02x}{:02x}{:02x}'.format(*rgb)

    def get_console_log(self):
        log = self.driver.get_log('browser')
        return log

    @staticmethod
    def current_timestamp(self):
        return int(time.time())


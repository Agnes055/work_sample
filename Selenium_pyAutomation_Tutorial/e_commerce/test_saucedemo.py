import re
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib3.util import wait


class TestUrl:
    Url = "https://www.saucedemo.com/"

@pytest.mark.usefixtures("initialize_browsers")
class BasesTest:
    pass
class TestSauce(BasesTest):

        # login with the valid credentials
    @pytest.mark.loginpage
    def invalid_login(self):
        self.driver.find_element(By.ID, "user-name").send_keys('standard_user')
        self.driver.find_element(By.ID, "password").send_keys('secret')
        self.driver.find_element(By.ID, "login-button").click()
        warning_message = self.driver.find_element(By.XPATH, "//h3[contains(text(),'Epic sadface')]").text
        expected_result = "Epic sadface: Username and password do not match any user in this service"
        assert warning_message == expected_result
        time.sleep(2)
    def valid_login(self):
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "user-name").send_keys('standard_user')
        self.driver.find_element(By.ID, "password").send_keys('secret_sauce')
        self.driver.find_element(By.ID, "login-button").click()
        assert self.driver.title == "Swag Labs", "page title is correct"
        time.sleep(2)

    # Function to add a product to the cart
    @pytest.mark.addtochart
    def add_to_cart(self):
        # wait = WebDriverWait(self.driver, 10)
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_to_cart_button.click()
        time.sleep(2)

    def add_to_cart1(self):
        add_to_cart_button = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
        add_to_cart_button.click()
        time.sleep(2)

    def add_to_cart2(self):
        add_to_cart_button = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_to_cart_button.click()
        time.sleep(2)

    def get_number_cart_items(self):
        # Use XPath to locate the element containing the cart count
        cart_count_element = self.driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container .shopping_cart_badge")

        # Get the text from the element
        cart_item_count = cart_count_element.text

        # Convert the text to an integer
        cart_item_count = int(cart_item_count)

        print(f"Number of items in the cart: {cart_item_count}")


    # Function to go to the checkout page
    @pytest.mark.checkout
    def add_to_cart_page(self):
        checkout_button = self.driver.find_element(By.XPATH, "//*[@id='shopping_cart_container']/a")
        checkout_button.click()
        time.sleep(2)


    def product_information(self):
        # Get the names or descriptions of the items in the cart
        cart_items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item_name")  # Example XPath

        # Example items that were added to the cart
        expected_items = ['Sauce Labs Backpack', 'Sauce Labs Fleece Jacket','Sauce Labs Bike Light']  # The items you expected to be added

        # Extract text from the cart items
        cart_item_names = [item.text for item in cart_items]

        # Assert that the expected items match the items in the cart
        assert sorted(cart_item_names) == sorted(
            expected_items), f"Cart items do not match. Found {cart_item_names}, expected {expected_items}"

        print("Assertion passed. Items in the cart are correct.")


    # click on the check out
    def checkout_page(self):
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()
        time.sleep(2)


    def invalid_checkout_details(self):
        # Find the input field (use an appropriate selector for your page)
        input_field = self.driver.find_element(By.ID, "first-name").send_keys("May123")
        input_field1 = self.driver.find_element(By.ID, "last-name").send_keys("Grace002")

        def validate_input_without_numbers(text):
            if re.search(r'\d', text):  # Checks if there's any digit in the text
                return False
            return True

        # Example text input
        text = "May123"

        # Validate the text before sending it
        if validate_input_without_numbers(text):
            # Send valid input to the field
            input_field.send_keys(text)
        else:
            print("Invalid input: first name contains numbers.")

        # def validate_input_without_numbers(text):
        #     if re.search(r'\d', text):  # Checks if there's any digit in the text
        #         return False
        #     return True

        # Example text input
        text = "Grace123"

        # Validate the text before sending it
        if validate_input_without_numbers(text):
            # Send valid input to the field
            input_field1.send_keys(text)
        else:
            print("Invalid input: Last name contains numbers.")

        self.driver.find_element(By.ID, "postal-code").send_keys("02")
        zip_code_value = self.driver.find_element(By.ID, "postal-code").get_attribute("value")
        zip_code_pattern = r'^\d{5}(-\d{4})?$'

        # Validate the zip code format using the regex pattern
        if re.match(zip_code_pattern, zip_code_value):
            print("Zip code format is correct!")
        else:
            print("Zip code format is not correct!")
        print(f"Entered zip code: {zip_code_value}")
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(2)

    def valid_checkout_details(self):
        self.driver.find_element(By.ID, "first-name").send_keys("May")
        self.driver.find_element(By.ID, "last-name").send_keys("Grace")
        self.driver.find_element(By.ID, "postal-code").send_keys("02234")
        zip_code_value = self.driver.find_element(By.ID, "postal-code").get_attribute("value")
        zip_code_pattern = r'^\d{5}(-\d{4})?$'

        # Validate the zip code format using the regex pattern
        if re.match(zip_code_pattern, zip_code_value):
            print("Zip code format is correct!")
        else:
            print("Zip code format is not correct!")
        print(f"Entered zip code: {zip_code_value}")
        self.driver.find_element(By.ID, "continue").click()
        time.sleep(2)

    def item_total_price(self):
        total_item_price = self.driver.find_element(By.CSS_SELECTOR, "#contents_wrapper .summary_subtotal_label")
        item_prices = total_item_price.text
        print(f"Total price of items in the cart: {item_prices}")
        assert item_prices == "Item total: $89.97"
    # function to finish the checkout process

    def total_itemandtax_price(self):
        total_item_tax_price = self.driver.find_element(By.CSS_SELECTOR, "#contents_wrapper .summary_total_label")
        tax_item_prices = total_item_tax_price.text
        print(f"Total price of items in the cart including tax: {tax_item_prices}")
        assert tax_item_prices == "Total: $97.17"

    def finish_page(self):
        checkout_button = self.driver.find_element(By.ID, "finish")
        checkout_button.click()
        time.sleep(2)

    # go back to the homepage
    @pytest.mark.homepage
    def go_back_home_page(self):
        checkout_button = self.driver.find_element(By.ID, "back-to-products")
        checkout_button.click()
        time.sleep(2)

    def three_line(self):
        three_line_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        three_line_button.click()
        time.sleep(2)

    def logout(self):
        logout = self.driver.find_element(By.ID, "logout_sidebar_link")
        logout.click()
        time.sleep(2)

    # run the functions
    @pytest.mark.skip(reason="this is not fully developed yet.")
    def test_invalid_login(self):
        self.invalid_login()

    def test_valid_login(self):
        self.valid_login()

    def test_add_to_cart(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()

    def test_get_number_cart_items(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
    def test_add_to_cart_page(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
    def test_product_information(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()

    def test_checkout_page(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()

    @pytest.mark.xfail(reason="first name, last name should not contain numbers")
    @pytest.mark.xfail(reason="zip code format should not be correct")
    def test_invalid_checkout_details(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.invalid_checkout_details()
    def test_valid_checkout_details(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.valid_checkout_details()
    def test_item_total_price(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.valid_checkout_details()
        self.item_total_price()
    def test_total_itemandtax_price(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.valid_checkout_details()
        self.item_total_price()
        self.total_itemandtax_price()

    def test_finish_page(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.valid_checkout_details()
        self.item_total_price()
        self.total_itemandtax_price()
        self.finish_page()

    def test_go_back_home_page(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.valid_checkout_details()
        self.item_total_price()
        self.total_itemandtax_price()
        self.finish_page()
        self.go_back_home_page()

    def test_three_line(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.valid_checkout_details()
        self.item_total_price()
        self.total_itemandtax_price()
        self.finish_page()
        self.go_back_home_page()
        self.three_line()

    def test_logout(self):
        self.valid_login()
        self.add_to_cart()
        self.add_to_cart1()
        self.add_to_cart2()
        self.get_number_cart_items()
        self.add_to_cart_page()
        self.product_information()
        self.checkout_page()
        self.valid_checkout_details()
        self.item_total_price()
        self.total_itemandtax_price()
        self.finish_page()
        self.go_back_home_page()
        self.three_line()
        self.logout()









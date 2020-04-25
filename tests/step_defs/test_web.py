import pytest
import time
from pytest_bdd import scenarios, given, when, then, parsers

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Constants
HOMEPAGE = 'http://localhost:5000'

# Scenarios
scenarios('../features/web.feature')


# Fixtures
@pytest.fixture
def browser(live_server):
    b = webdriver.Firefox()
    yield b
    b.quit()


# Given Steps
@given('the homepage is displayed')
def application_homepage(browser):
    browser.get(HOMEPAGE)

@given(parsers.parse('there is tip titled "{title}"'))
def tip_exists(browser, title):
    xpath = "//div[@id='tip-list-item']//*[contains(text(), '%s')]" % title
    results = browser.find_elements_by_xpath(xpath)


# When Steps
@when(parsers.parse('the user enters title "{title}"'))
def enter_title(browser, title):
    search_input = browser.find_element_by_id('input-Otsikko')
    search_input.send_keys(title)


@when("user clicks save button")
def click_save(browser):
    save_button = browser.find_element_by_id('button-add-tip')
    save_button.click()

@when(parsers.parse('user clicks remove button of "{title}"'))
def click_remove(browser, title):
    xpath = "//*[contains(text(), '%s')]/ancestor::*[@id='tip-list-item']//*[@id='button-remove-tip']" % title
    remove_button = browser.find_elements_by_xpath(xpath)
    remove_button[0].click()

@when("user confirms delete")
def confirm_remove(browser):
    browser.switch_to.alert.accept()


# Then Steps
@then(parsers.parse('"{title}" should be added to the list'))
def results_have_title(browser, title):
    time.sleep(1)
    xpath = "//div[@id='tip-list-item']//*[contains(text(), '%s')]" % title
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

@then(parsers.parse('"{title}" should not appear in the list'))
def results_have_title(browser, title):
    time.sleep(1)
    xpath = "//div[@id='tip-list-item']//*[contains(text(), '%s')]" % title
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) == 0
    
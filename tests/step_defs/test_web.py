import pytest
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
    b.implicitly_wait(3)

    yield b
    b.quit()


# Given Steps
@given('the homepage is displayed')
def application_homepage(browser):
    browser.get(HOMEPAGE)
    browser.implicitly_wait(5)


# When Steps
@when(parsers.parse('the user enters title "{title}"'))
def enter_title(browser, title):
    search_input = browser.find_element_by_id('tip_url')
    search_input.send_keys(title + Keys.RETURN)


@when("user clicks save button")
def click_save(browser):
    save_button = browser.find_elements_by_xpath('Lisää')
    save_button.click()


# Then Steps
@then(parsers.parse('"{title}" should be added to the list'))
def results_have_title(browser, title):
    xpath = "//div[@id='tip-list-item']//*[contains(text(), '%s')]" % title
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

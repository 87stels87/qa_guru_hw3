import pytest
from selene import have, be
from selene.support.shared import browser


@pytest.fixture
def browser_setup():
    browser.open('https://duckduckgo.com')
    browser.driver.maximize_window()
    yield
    browser.quit()


def test_succesfull_search(browser_setup):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python - GitHub'))


def test_unsuccessful_search(browser_setup):
    browser.element('[name="q"]').should(be.blank).type('_____!').press_enter()
    browser.element('html').should(have.text('результаты не найдены.'))

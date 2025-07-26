from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("https://github.com")

    s('.header-search-button').click()
    s('#query-builder-test').type("eroshenkoam/allure-example").submit()
    s('[href="/eroshenkoam/allure-example"]').click()
    s("[data-content='Pull requestss']").click()
    s(by.partial_text("#91")).should(be.visible)
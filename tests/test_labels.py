import allure
from selene import by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Кликаем в поле поиска"):
        s('.header-search-button').click()

    with allure.step("Вводим текст в поле поиска"):
        s('#query-builder-test').type("eroshenkoam/allure-example").submit()

    with allure.step("Открываем репозиторий allure-example"):
        s('[href="/eroshenkoam/allure-example"]').click()

    with allure.step("Открываем раздел Pull requests"):
        s("[data-content='Pull requests']").click()

    with allure.step("Ищем на странице request с номером 91"):
        s(by.partial_text("#91")).should(be.visible)

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository()
    open_pull_requests_tab()
    should_visible_repository("91")

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').type(repo).submit()

@allure.step("Переходим по ссылке репозитория")
def go_to_repository():
    s('[href="/eroshenkoam/allure-example"]').click()

@allure.step("Переходим по ссылке репозитория")
def open_pull_requests_tab():
    s("[data-content='Pull requests']").click()

@allure.step("Ищем на странице request с номером {number}")
def should_visible_repository(number):
    s(by.partial_text("#" + number)).should(be.visible)


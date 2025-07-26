import time

import allure
from allure_commons.types import Severity
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from homework.model.pages.issue_page import IssuePage

issue_page = IssuePage()

def test_issue_clear_selene():
    browser.open("https://github.com")

    s('.header-search-button').click()
    s('#query-builder-test').type("allure").submit()
    s('[href="/allure-framework/allure2"]').click()
    s('#issues-tab').click()
    s('[data-testid="issue-pr-title-link"]').should(have.exact_text('Allure Dashboard overview shows incorrect testcase count with Pabot Robot Framework runs'))

def test_issue_lambda():
    with allure.step("Открываем сайт github"):
        browser.open("https://github.com")

    with allure.step("Открываем репозиторий allure-framewokr/allure2"):
        s('.header-search-button').click()
        s('#query-builder-test').type("allure").submit()
        s('[href="/allure-framework/allure2"]').click()

    with allure.step("Открываем issue-tab"):
        s('#issues-tab').click()

    with allure.step("Ищем issue с названием Allure Dashboard overview shows incorrect testcase count with Pabot Robot Framework runs"):
        s('[data-testid="issue-pr-title-link"]').should(
            have.exact_text('Allure Dashboard overview shows incorrect testcase count with Pabot Robot Framework runs'))

def test_issue_decorator():
    issue_page.open_main_page()
    issue_page.search_for_repository()
    issue_page.open_issue_tab()
    issue_page.should_visible_issue(name="Allure Dashboard overview shows incorrect testcase count with Pabot Robot Framework runs")

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "rominikhom")
@allure.feature("Issue в репозитории")
@allure.story("Поиск наименования issue в репозитории")
@allure.link("https://github.com", name="github")
def test_issue_labels():
    issue_page.open_main_page()
    issue_page.search_for_repository()
    issue_page.open_issue_tab()
    issue_page.should_visible_issue(
        name="Allure Dashboard overview shows incorrect testcase count with Pabot Robot Framework runs")


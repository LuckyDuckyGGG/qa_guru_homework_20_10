import allure
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

class IssuePage:

    @allure.step("Открываем сайт github")
    def open_main_page(self):
        browser.open("https://github.com")

    @allure.step("Открываем репозиторий allure-framework/allure2")
    def search_for_repository(self):
        s('.header-search-button').click()
        s('#query-builder-test').type("allure").submit()
        s('[href="/allure-framework/allure2"]').click()

    @allure.step("Открываем issue-tab")
    def open_issue_tab(self):
        s('#issues-tab').click()

    @allure.step("Ищем на странице issue с названием")
    def should_visible_issue(self, name):
        s('[data-testid="issue-pr-title-link"]').should(
            have.exact_text(name))
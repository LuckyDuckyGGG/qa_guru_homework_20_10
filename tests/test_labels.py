import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задача в репозитории")
    allure.dynamic.story("Неавторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")
    pass

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", )
@allure.feature("Задачи")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass


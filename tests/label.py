import allure
from allure_commons.types import Severity


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.feature('Issues')
    allure.dynamic.story('Create')
    allure.dynamic.link('https://github.com', name='Github')
    allure.dynamic.title('Проверка работы анотации')
    pass


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.feature('Issues')
@allure.story('Create')
@allure.link('https://github.com', name='Github')
@allure.title('Создание issue')

def test_decorator_lables():
    pass
import allure
from allure_commons.types import Severity
from selene import browser, by, be

@allure.tag('mobile')
@allure.severity(Severity.BLOCKER)
@allure.feature('Issues #1')
@allure.story('Search')
@allure.link('https://github.com', name='Github')
@allure.title('проверка аннотаций в тесте')

def test_github_steps():
    with allure.step('Открыть \'github.com\''):
        browser.open('https://github.com')

    with allure.step(
            'Выполнить поиск \'eroshenkoam/allure-example\''
    ):
        browser.element('.search-input-container').click()
        browser.element('#query-builder-test').send_keys(
            'eroshenkoam/allure-example'
        ).submit()

    with allure.step('Выбрать \'eroshenkoam/allure-example\''):
        browser.element(by.link_text('eroshenkoam/allure-playwright-example')).click()

    with allure.step('Перейти в issues'):
        browser.element('#issues-tab').click()

    with allure.step('Находим Issue с номером #1'):
        browser.element('span.issue-item-module__defaultNumberDescription--GXzri > span').should(be.visible)


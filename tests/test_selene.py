from selene.support import by
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_github():
    browser.open("https://github.com")

    s('.search-input-container').click()
    s('#query-builder-test').send_keys("eroshenkoam/allure-example")
    s('#query-builder-test').submit()
    s(by.link_text("eroshenkoam/allure-playwright-example")).click()
    s("#issues-tab").click()
    s('span.issue-item-module__defaultNumberDescription--GXzri > span').should(have.text("#1"))

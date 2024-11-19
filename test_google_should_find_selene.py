from selene import browser, be, have

def test_search_positive():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_negative():
    browser.element('[name="q"]').should(be.blank).type('sdfsdfsdfsdfsdfasdasassasdaseq23213213').press_enter()
    browser.element('[id="botstuff"]').should(have.text('did not match any documents'))

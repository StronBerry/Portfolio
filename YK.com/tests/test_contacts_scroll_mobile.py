import time
from pages.main_page import MainPage

def test_scroll_to_contacts_mobile(browser):
    """Проверка перехода к якорю 'КОНТАКТЫ' из мобильного меню"""
    browser.set_window_size(375, 800)
    time.sleep(1)

    page = MainPage(browser)
    page.open()

    assert page.is_visible(MainPage.BURGER_BUTTON), "Бургер-меню не отображается"
    page.click(MainPage.BURGER_BUTTON)
    time.sleep(1)

    assert page.is_visible(MainPage.CONTACTS_LINK_MOBILE), "Ссылка 'КОНТАКТЫ' не найдена в меню"
    page.click(MainPage.CONTACTS_LINK_MOBILE)
    time.sleep(2)  # дожидаемся прокрутки

    assert page.is_visible(MainPage.CONTACTS_BLOCK_TITLE), "Заголовок блока 'Контакты' не отображается"

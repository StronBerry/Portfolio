import pytest
from pages.main_page import MainPage


def test_main_page_loads(browser):
    """Проверка успешной загрузки главной страницы сайта"""
    page = MainPage(browser)
    page.open()

    assert page.is_visible(MainPage.HEADER_TITLE), "Главный заголовок не найден — страница могла не загрузиться"

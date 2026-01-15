import pytest
from pages.main_page import MainPage

@pytest.mark.parametrize("width,height,label", [
    (1920, 1080, "десктоп"),
    (768, 1024, "планшет"),
    (375, 667, "мобильный"),
])
def test_main_page_responsive(browser, width, height, label):
    """Проверка адаптивности главной страницы: заголовок отображается на всех типах устройств"""
    browser.set_window_size(width, height)
    page = MainPage(browser)
    page.open()

    assert page.is_visible(MainPage.HEADER_TITLE), f"Заголовок не найден при разрешении {label} ({width}x{height})"

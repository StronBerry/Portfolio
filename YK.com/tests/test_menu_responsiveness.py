import pytest
import time
from pages.main_page import MainPage

@pytest.mark.parametrize("width,expected_menu", [
    (1024, "full"),   # Десктоп
    (980, "burger"),  # Планшет
    (375, "burger"),  # Мобильный
])
def test_menu_responsiveness(browser, width, expected_menu):
    """Проверка адаптивности меню: отображение полного меню или бургер-меню в зависимости от ширины экрана"""
    browser.set_window_size(width, 800)
    time.sleep(1)  # Подождать перестройки DOM

    page = MainPage(browser)
    page.open()

    if expected_menu == "full":
        assert page.is_visible(MainPage.FULL_MENU), f"Полное меню не отображается при ширине {width}px"
        assert not page.is_visible(MainPage.BURGER_BUTTON), f"Бургер-меню не должно отображаться при ширине {width}px"
    else:
        assert page.is_visible(MainPage.BURGER_BUTTON), f"Бургер-меню не отображается при ширине {width}px"
        assert not page.is_visible(MainPage.FULL_MENU), f"Полное меню не должно отображаться при ширине {width}px"

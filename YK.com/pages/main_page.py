from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    URL = "https://yuliakonovalova.com/"

    HEADER_TITLE = (By.XPATH, "//h1[contains(@class, 'tn-atom')]//*[contains(text(), 'Консультант по корпоративному обучению')]") #h1
    FULL_MENU = (By.CSS_SELECTOR, ".t228__list")  # Полное меню
    BURGER_BUTTON = (By.CSS_SELECTOR, "button.t-menuburger") # Бургер кнопка
    CONTACTS_LINK_MOBILE = (By.LINK_TEXT, "КОНТАКТЫ")
    CONTACTS_BLOCK_TITLE = (
        By.XPATH,
        "//div[contains(@class, 't-title') and contains(., 'КОНТАКТЫ')]"
    )

    def open(self):
        self.driver.get(self.URL)

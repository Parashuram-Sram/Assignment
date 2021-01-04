from Locators import Common as Locator
from Pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_nav_sections(self, nav_id):
        header = self.driver.find_element_by_id(nav_id)
        sections = header.find_elements_by_css_selector(Locator.Top_Nav_Sections_Class)
        return [sec.text for sec in sections]

    def get_top_nav_sections(self):
        return self.get_nav_sections(Locator.Top_Nav_Id)

    def get_sub_nav_sections(self):
        sub_menu = self.driver.find_element_by_id(Locator.Sub_Menu_Id)
        sub_menu.click()
        return self.get_nav_sections(Locator.Sub_Nav_Id)

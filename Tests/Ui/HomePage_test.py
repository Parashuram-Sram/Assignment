from collections import Counter
import pytest
from Data import TestData
from Pages.HomePage import HomePage


@pytest.mark.usefixtures("driver")
class TestHomePage:

    @pytest.mark.regression
    def test_home_page_title(self):
        home_page = HomePage(self.driver)
        assert home_page.get_title() == TestData.Home_Page_Title

    @pytest.mark.regression
    def test_home_page_top_nav_sections(self):
        home_page = HomePage(self.driver)
        top_nav_actual = home_page.get_top_nav_sections()
        top_nav = TestData.Home_Page_Top_Nav_Sections
        assert Counter(top_nav_actual) == Counter(top_nav)

    @pytest.mark.regression
    @pytest.mark.parametrize("sec", ['WEATHER', 'TV SCHEDULE'])
    def test_home_page_sub_nav_sections(self, sec):
        home_page = HomePage(self.driver)
        sub_nav_sections = home_page.get_sub_nav_sections()
        assert sec in sub_nav_sections
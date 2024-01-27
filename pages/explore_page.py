from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page


class ExplorePage(Page):
    SEARCH_ICON = (AppiumBy.XPATH, "//*[@content-desc='Search Wikipedia']")
    CUSTOMIZE = (AppiumBy.ID, "org.wikipedia:id/view_announcement_action_positive")

    def click_search_icon(self):
        self.tap(*self.SEARCH_ICON)


    def customize_explore_feed(self):
        self.tap(*self.CUSTOMIZE)

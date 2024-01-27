from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy



@when("Open Customize Explore Feed")
def customize_feed(context):
    context.app.explore_page.customize_explore_feed()


@then("Verify {text} on Explore Feed is not found")
def verify_customize_found_on_home(context, text):
    text = (AppiumBy.ID, "//*[contains(text(), text)]")
    context.app.page.wait_for_element_disappear(*text)

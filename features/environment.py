from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.chrome.options import Options
from app.application import Application


def mobile_driver_init(context, scenario_name):
    """
    :param context: Behave context
    """
    # desired_capabilities = {
    #     "platformName": "Android",
    #     "automationName": 'uiautomator2',
    #     "platformVersion": "10",
    #     "deviceName": "Android Emulator",
    #     "appActivity": "org.wikipedia.main.MainActivity",
    #     "appPackage": "org.wikipedia",
    #     # Put your path below:
    #     "app": "C:/Users/noahsj/AppiumAutomation/mobile_app/wikipedia.apk"
    # }
    #
    # appium_server_url = 'http://localhost:4723'
    # capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)
    #
    # context.driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    # context.driver.implicitly_wait(5)
    #
    # context.app = Application(context.driver)


###BROWSERSTACK###
    bs_user = 'noahsj_p3KDFs',
    bs_key = 'BAiKTuqj9kkQtzaDyRBE',
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    app = 'bs://6ef5bd11a08f26d8ca4a095c5b7dc85d5e8b1c64',
    options = Options()
    browserstack_caps = {
        # 'browserstack.networkLogs': 'true',
        'device': 'Samsung Galaxy S21',
        'os_version': '11.0',
        'automationName': 'UiAutomator2',
        'project': 'Appium Wiki Test',
        'build': 'Python Android',
        'name': scenario_name
    }
    options.set_capability('bstack:options', browserstack_caps)
    context.browserstack_driver = webdriver.Remote('http://hub-cloud.browserstack.com/wd/hub', options=options)
    context.driver.implicitly_wait(5)
    context.app = Application(context.browserstack_driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    mobile_driver_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        # context.driver.save_screenshot(f'{step}.png')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    # context.driver.quit()
    context.browserstack_driver.quit()


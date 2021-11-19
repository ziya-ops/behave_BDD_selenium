from behave import *
from selenium import webdriver


@given(u'Launch chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
    # Supported latest chromedriver exe available in python installation scripts path
    context.driver = webdriver.Chrome()


@when(u'open facebook home page')
def OpenHomePage(context):
    context.driver.get("https://www.facebook.com/")


@then(u'verify that logo is present on home page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//img[@alt='Facebook']").is_displayed()
    assert status is True


# @then(u'Close browser')
# def closeBrowser(context):
#     context.driver.close()

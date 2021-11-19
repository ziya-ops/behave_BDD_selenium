from behave import *
from selenium import webdriver


# @given(u'Launch chrome browser')
# def launchBrowser(context):
#     # context.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
#     # Supported latest chromedriver exe available in python installation scripts path
#     context.driver = webdriver.Chrome()
#
#
# @when(u'open facebook home page')
# def OpenHomePage(context):
#     context.driver.get("https://www.facebook.com/")


@when(u'Enter email "{user}" and password "{pwd}"')
def enterCredentials(context, user, pwd):
    context.driver.find_element_by_id("email").send_keys(user)
    context.driver.find_element_by_id("pass").send_keys(pwd)


@when(u'Click Login button')
def clickLogin(context):
    context.driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()


@then(u'verify Login failure error msg')
def verifyLogin(context):
    text = context.driver.find_element_by_xpath("//a[contains(text(),'Find your account and log in.')]").text
    assert text == "Find your account and log in"


@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

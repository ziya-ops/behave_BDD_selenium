from behave import *
from selenium import webdriver


@given(u'hrm- Launch chrome browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome(executable_path="C:\\drivers\\chromedriver.exe")
    # Supported latest chromedriver exe available in python installation scripts path
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'hrm- open orangehrm home page')
def OpenHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'hrm- Enter username {user} and password {pwd}')
def enterCredentials(context, user, pwd):
    context.driver.find_element_by_id("txtUsername").send_keys(user)
    context.driver.find_element_by_id("txtPassword").send_keys(pwd)


@when(u'hrm- Click Login button')
def clickLogin(context):
    context.driver.find_element_by_id("btnLogin").click()


@then(u'hrm -verify Login success or failure')
def loginVerify(context):
    try:
        text = context.driver.find_element_by_xpath("//h1[contains(text(),'Dashboard')]").text
    except:
        context.driver.close()
        assert False, "Login Failed"

    if text == "Dashboard":
        assert True, "Login Successful"
        # context.driver.close()


# @then(u'hrm -Close browser')
# def closeBrowser(context):
#     context.driver.close()

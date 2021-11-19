from behave import *


@then(u'hrm- Print background executed')
def step_impl(context):
    assert True, "Background Executed"


@then(u'print first scenario success')
def step_impl(context):
    assert True, "first scenario success"


@then(u'print second scenario success')
def step_impl(context):
    assert True, "second scenario success"


@then(u'print third scenario success')
def step_impl(context):
    assert True, "third scenario success"

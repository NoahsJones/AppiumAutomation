from behave import given, when, then


@when("Go back")
def go_back(context):
    context.app.page.go_back()
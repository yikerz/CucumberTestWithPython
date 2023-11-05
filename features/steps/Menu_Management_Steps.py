import sys
sys.path.insert(0, r'C:\Users\Yik\Desktop\CucumberTestWithPython')
from models.MenuItem import MenuItem
from models.Menu import Menu
from behave import given, when, then

@given(u'I have a menu item with name "{name}" and price {price}')
def step_impl(context, name, price):
    context.menu = Menu()
    context.item = MenuItem(name, price)

@when(u'I add the item into the menu')
def step_impl(context):
    try:
        context.menu.add_item(context.item)
    except ValueError as e:
        error_msg = str(e)
        print(error_msg, file=sys.stderr)
        
@then(u'The menu should include the item "{name}"')
def step_impl(context, name):
    assert context.menu.doesItemExist(name) == True

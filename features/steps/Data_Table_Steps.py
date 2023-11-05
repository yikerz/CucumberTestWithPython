from behave import given, when, then
import math

@given(u'I placed an order for the following items as table')
def step_impl(context):
    context.sum = 0
    for r in context.table:
        context.sum += float(r['Units']) * float(r['UnitPrice'])
    
@when(u'I generate the bill')
def step_impl(context):
    pass


@then(u'A bill for {expected_total} should be generated')
def step_impl(context, expected_total):
    expected_total = float(expected_total)
    assert math.isclose(context.sum, expected_total, rel_tol=1e-3)


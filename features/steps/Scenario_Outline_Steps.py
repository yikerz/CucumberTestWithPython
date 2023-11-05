import sys
sys.path.insert(0, r'C:\Users\Yik\Desktop\CucumberTestWithPython')
from models.TaxCalculator import TaxCalculator
from behave import given, then
import math

@given(u'I have a Customer')
def step_impl(context):
    pass

@given(u'User enters initial bill amount as {initial_bill_amount}')
def step_impl(context, initial_bill_amount):
    context.initial_bill_amount = float(initial_bill_amount)
    

@given(u'Sales Tax Rate is {tax_rate} Percent')
def step_impl(context, tax_rate):
    context.tax_rate = float(tax_rate)

@then(u'Final bill amount calculated is {expected_total}')
def step_impl(context, expected_total):
    expected_total = float(expected_total)
    actual_total = TaxCalculator.calculate_total_bill(context.initial_bill_amount, context.tax_rate)
    assert math.isclose(actual_total, expected_total, rel_tol=1e-3)
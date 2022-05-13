from unittest import TestCase
from checkout_calculator import CheckoutCalculator

class TestCheckoutCalculatorCalculateTotals(TestCase):
  def setUp(self):
    self.checkout_calculator = CheckoutCalculator(
      products = {
        'book': { 'price': 1.50 },
        'chair': { 'price': 3 },
        'desk': { 'price': 10.32 }
      }
    )

  def test_calculate_totals_when_items_is_not_populated(self):
    'When the data member `items` is not_populated, it returns with totals of `0`'

    self.assertDictEqual(
      self.checkout_calculator.calculate_totals(items = []),
      { 'subtotal': 0, 'sales_tax_total': 0, 'sales_tax_rate': 0, 'total': 0 }
    )

  def test_calculate_totals_when_items_is_populated(self):
    'When the data member `items` is populated, it returns the `checkout_total`'

    items = [
      { 'product_key': 'book', 'count': 3 },
      { 'product_key': 'desk', 'count': 5 },
      { 'product_key': 'chair', 'count': 2 }
    ]
    sales_tax_rate = 0.1
    expected_subtotal = (3 * 1.50) + (5 * 10.32) + (2 * 3)
    expected_sales_tax_total = expected_subtotal * sales_tax_rate
    expected_total = expected_subtotal + expected_sales_tax_total

    self.assertDictEqual(
      self.checkout_calculator.calculate_totals(items = items, sales_tax_rate = sales_tax_rate),
      {
        'subtotal': expected_subtotal,
        'sales_tax_total': expected_sales_tax_total,
        'sales_tax_rate': sales_tax_rate,
        'total': expected_total
      }
    )

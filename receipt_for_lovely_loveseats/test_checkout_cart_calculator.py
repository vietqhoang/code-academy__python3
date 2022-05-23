'Unit test for CheckoutCartCalculator class'

from unittest import TestCase
from unittest.mock import patch
from checkout_cart_calculator import CheckoutCartCalculator

class TestCheckoutCartCalculatorInitValidations(TestCase):
    'Unit test for CheckoutCartCalculator validation calls on initialization'

    @patch('checkout_cart_calculator.CheckoutCartCalculator._validate_shape_of_products')
    def test_validate_shape_of_products_is_called(self, mock):
        CheckoutCartCalculator(products = {})
        self.assertTrue(mock.called)

class TestCheckoutCartCalculatorCalculateTotals(TestCase):
    'Unit test for CheckoutCartCalculator.calculate_totals'

    def setUp(self):
        self.subject = CheckoutCartCalculator(
            products = {
                'book': { 'price': 1.50, 'name': 'A book', 'description': 'It is made of paper' },
                'chair': { 'price': 3 , 'name': 'A chair', 'description': 'It is made of wood'},
                'desk': { 'price': 10.32, 'name': 'A desk', 'description': 'It is made of water' }
            }
        ).calculate_totals

    def test_calculate_totals_when_items_is_not_populated(self):
        'When the data member `items` is not_populated, it returns with totals of `0`'

        self.assertDictEqual(
            self.subject(items = []),
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
            self.subject(
                items = items,
                sales_tax_rate = sales_tax_rate
            ),
            {
                'subtotal': expected_subtotal,
                'sales_tax_total': expected_sales_tax_total,
                'sales_tax_rate': sales_tax_rate,
                'total': expected_total
            }
        )

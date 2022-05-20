'Unit test for Receipt class'

from unittest import TestCase
from unittest.mock import patch
from receipt import Receipt

class TestReceiptInitValidations(TestCase):
    'Unit test for Receipt validation calls on initialization'

    @patch('receipt.Receipt._validate_shape_of_products')
    def test_validate_shape_of_products_is_called(self, mock):
        Receipt(products = {})
        self.assertTrue(mock.called)

class TestReceiptReceiptBody(TestCase):
    'Unit test for Receipt.receipt.body'

    def setUp(self):
        self.subject = Receipt(
            products = {
                'book': {
                    'name': 'If You Give A Mouse A Cookie',
                    'description': "A children's book about a mouse who likes cookies.",
                    'price': 2.2
                },
                'chair': {
                    'name': 'Herman Miller Eames Lounge Chair',
                    'description': 'You probably can not afford it.',
                    'price': 1
                },
                'desk': {
                    'name': 'Fully Jarvis Standing Desk',
                    'description': 'It is a pretty good desk!',
                    'price': 4.40
                }
            }
        ).receipt_body

    @classmethod
    def setUpClass(cls):
        cls.items = [
            { 'product_key': 'book', 'count': 2 },
            { 'product_key': 'chair', 'count': 88 }
        ]
        cls.totals = {
            'subtotal': 2.0,
            'sales_tax_total': 0.54,
            'sales_tax_rate': 0.27,
            'total': 2.54
        }

    def test_receipt_receipt_body(self):
        'Returns the generated receipt body'

        expected_body = (
            'Customer Items:\n'
            '* 2x If You Give A Mouse A Cookie: '
            "A children's book about a mouse who likes cookies.\n"
            '* 88x Herman Miller Eames Lounge Chair: You probably can not afford it.\n'
            '\n'
            'Subtotal: $2.00\n'
            'Sales tax (27.00%): $0.54\n'
            'Total: $2.54'
        )

        self.assertEqual(
            self.subject(items = self.items, totals = self.totals),
            expected_body
        )

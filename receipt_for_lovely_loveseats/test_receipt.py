'Unit test for Receipt class'

from unittest import TestCase
from receipt import Receipt

class TestReceiptReceiptBody(TestCase):
    'Unit test for Receipt.receipt.body'

    def setUp(self):
        self.receipt = Receipt(
            products = {
                'book': {
                    'name': 'If You Give A Mouse A Cookie',
                    'description': "A children's book about a mouse who likes cookies."
                },
                'chair': {
                    'name': 'Herman Miller Eames Lounge Chair',
                    'description': 'You probably can not afford it.'
                },
                'desk': {
                    'name': 'Fully Jarvis Standing Desk',
                    'description': 'It is a pretty good desk!'
                }
            }
        )

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
            self.receipt.receipt_body(items = self.items, totals = self.totals),
            expected_body
        )

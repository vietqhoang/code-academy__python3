'Unit test for CheckoutCart class'

from unittest import TestCase
from checkout_cart import CheckoutCart

class TestCheckoutCartAddToCheckout(TestCase):
    'Unit test for CheckoutCart.add_to_checkout'

    def setUp(self):
        self.subject_cls = CheckoutCart(products = { 'book': {}, 'chair': {}, 'desk': {}})
        self.subject = self.subject_cls.add_to_checkout

    def test_add_to_checkout_returns_current_checkout_list(self):
        (
            'When a product and subsequent products are added to checkout, '
            'the returned checkout list reflects the current items'
        )

        self.assertCountEqual(
            self.subject(product_key = 'book', count = 2),
            [{ 'product_key': 'book', 'count': 2 }]
        )

        self.assertCountEqual(
            self.subject(product_key = 'desk', count = 1),
            [
                { 'product_key': 'book', 'count': 2 },
                { 'product_key': 'desk', 'count': 1 }
            ]
        )

        self.assertCountEqual(
            self.subject(product_key = 'desk', count = 3),
            [
                { 'product_key': 'book', 'count': 2 },
                { 'product_key': 'desk', 'count': 4 }
            ]
        )

    def test_add_to_checkout_updates_current_checkout_list(self):
        (
            'When a product and subsequent products are added to checkout, '
            'the `items` data member is updated to reflect the added product'
        )


        self.subject(product_key = 'book', count = 4)
        self.assertCountEqual(
            self.subject_cls.items,
            [{ 'product_key': 'book', 'count': 4 }]
        )

        self.subject(product_key = 'desk', count = 2)
        self.assertCountEqual(
            self.subject_cls.items,
            [
                { 'product_key': 'book', 'count': 4 },
                { 'product_key': 'desk', 'count': 2 }
            ]
        )

        self.subject(product_key = 'book', count = 3)
        self.assertCountEqual(
            self.subject_cls.items,
            [
                { 'product_key': 'book', 'count': 7 },
                { 'product_key': 'desk', 'count': 2 }
            ]
        )

class TestCheckoutRemoveFromCheckout(TestCase):
    'Unit test for CheckoutCart.remove_from_checkout'

    def setUp(self):
        self.subject_cls = CheckoutCart(
            products = { 'book': {}, 'chair': {}, 'desk': {} },
            items = [
                { 'product_key': 'chair', 'count': 8 },
                { 'product_key': 'desk', 'count': 15 }
            ]
        )
        self.subject = self.subject_cls.remove_from_checkout

    def test_remove_from_checkout_returns_current_checkout_list(self):
        (
            'When a product and subsequent products are removed from checkout, '
            'the returned checkout list reflects the current items'
        )

        self.assertCountEqual(
            self.subject(product_key = 'chair', count = 2),
            [
                { 'product_key': 'chair', 'count': 6 },
                { 'product_key': 'desk', 'count': 15 }
            ]
        )

        self.assertCountEqual(
            self.subject(product_key = 'desk', count = 15),
            [{ 'product_key': 'chair', 'count': 6 }]
        )

        self.assertCountEqual(
            self.subject(product_key = 'chair', count = 8),
            []
        )

        self.assertCountEqual(
            self.subject(product_key = 'chair', count = 3),
            []
        )

    def test_remove_from_checkout_updates_current_checkout_list(self):
        (
            'When a product and subsequent products are removed from checkout, '
            'the `items` data member is updated to reflect the removed product'
        )

        self.subject(product_key = 'chair', count = 4)
        self.assertCountEqual(
            self.subject_cls.items,
            [
                { 'product_key': 'chair', 'count': 4 },
                { 'product_key': 'desk', 'count': 15 }
            ]
        )

        self.subject(product_key = 'chair', count = 4)
        self.assertCountEqual(
            self.subject_cls.items,
            [{ 'product_key': 'desk', 'count': 15 }]
        )

        self.subject(product_key = 'desk', count = 15)
        self.assertCountEqual(self.subject_cls.items, [])

        self.subject(product_key = 'desk', count = 3)
        self.assertCountEqual(self.subject_cls.items, [])

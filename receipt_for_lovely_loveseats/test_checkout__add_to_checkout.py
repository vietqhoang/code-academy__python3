from unittest import TestCase
from checkout import Checkout

class TestCheckoutAddToCheckout(TestCase):
  def setUp(self):
    self.checkout = Checkout(products = { 'book': {}, 'chair': {}, 'desk': {}}, items = [])

  def test_add_to_checkout_returns_current_checkout_list(self):
    'When a product and subsequent products are added to checkout, the returned checkout list reflects the current items'

    self.assertCountEqual(
      self.checkout.add_to_checkout(product_key = 'book', count = 2),
      [{ 'product_key': 'book', 'count': 2 }]
    )

    self.assertCountEqual(
      self.checkout.add_to_checkout(product_key = 'desk', count = 1),
      [
        { 'product_key': 'book', 'count': 2 },
        { 'product_key': 'desk', 'count': 1 }
      ]
    )

    self.assertCountEqual(
      self.checkout.add_to_checkout(product_key = 'desk', count = 3),
      [
        { 'product_key': 'book', 'count': 2 },
        { 'product_key': 'desk', 'count': 4 }
      ]
    )

  def test_add_to_checkout_updates_current_checkout_list(self):
    'When a product and subsequent products are added to checkout, the `items` data member is updated to reflect the added product'

    self.checkout.add_to_checkout(product_key = 'book', count = 4)
    self.assertCountEqual(
      self.checkout.items,
      [{ 'product_key': 'book', 'count': 4 }]
    )

    self.checkout.add_to_checkout(product_key = 'desk', count = 2)
    self.assertCountEqual(
      self.checkout.items,
      [
        { 'product_key': 'book', 'count': 4 },
        { 'product_key': 'desk', 'count': 2 }
      ]
    )

    self.checkout.add_to_checkout(product_key = 'book', count = 3)
    self.assertCountEqual(
      self.checkout.items,
      [
        { 'product_key': 'book', 'count': 7 },
        { 'product_key': 'desk', 'count': 2 }
      ]
    )

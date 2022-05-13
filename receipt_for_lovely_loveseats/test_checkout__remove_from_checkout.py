from unittest import TestCase
from checkout import Checkout

class TestCheckoutRemoveFromCheckout(TestCase):
  def setUp(self):
    self.checkout = Checkout(
      products = { 'book': {}, 'chair': {}, 'desk': {} },
      items = [
        { 'product_key': 'chair', 'count': 8 },
        { 'product_key': 'desk', 'count': 15 }
      ]
    )

  def test_remove_from_checkout_returns_current_checkout_list(self):
    'When a product and subsequent products are removed from checkout, the returned checkout list reflects the current items'

    self.assertCountEqual(
      self.checkout.remove_from_checkout(product_key = 'chair', count = 2),
      [
        { 'product_key': 'chair', 'count': 6 },
        { 'product_key': 'desk', 'count': 15 }
      ]
    )

    self.assertCountEqual(
      self.checkout.remove_from_checkout(product_key = 'desk', count = 15),
      [
        { 'product_key': 'chair', 'count': 6 }
      ]
    )

    self.assertCountEqual(
      self.checkout.remove_from_checkout(product_key = 'chair', count = 8),
      []
    )

    self.assertCountEqual(
      self.checkout.remove_from_checkout(product_key = 'chair', count = 3),
      []
    )

  def test_remove_from_checkout_updates_current_checkout_list(self):
    'When a product and subsequent products are removed from checkout, the `items` data member is updated to reflect the removed product'

    self.checkout.remove_from_checkout(product_key = 'chair', count = 4)
    self.assertCountEqual(
      self.checkout.items,
      [
        { 'product_key': 'chair', 'count': 4 },
        { 'product_key': 'desk', 'count': 15 }
      ]
    )

    self.checkout.remove_from_checkout(product_key = 'chair', count = 4)
    self.assertCountEqual(
      self.checkout.items,
      [
        { 'product_key': 'desk', 'count': 15 }
      ]
    )

    self.checkout.remove_from_checkout(product_key = 'desk', count = 15)
    self.assertCountEqual(
      self.checkout.items,
      []
    )

    self.checkout.remove_from_checkout(product_key = 'desk', count = 3)
    self.assertCountEqual(
      self.checkout.items,
      []
    )

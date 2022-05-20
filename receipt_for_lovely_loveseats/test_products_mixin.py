'Unit test for ProductsMixin class'

from unittest import TestCase
from products_mixin import ProductsMixin

class TestProductsMixinValidateShapeOfProducts(TestCase):
  'Unit tests for ProductMixin._validate_shape_of_products'

  def setUp(self):
    self.subject = ProductsMixin()._validate_shape_of_products

  def test_validate_shape_of_products_minimal_valid(self):
    try:
      self.subject(products = {})
    except:
      self.fail('`_validate_shape_of_products` raised an exception')

  def test_validate_shape_of_products_is_valid(self):
    try:
      self.subject(
        products = {
          'book': { 'name': 'Harry Potter', 'price': 1.00, 'description': 'Kids playing with sticks' },
          'magazine': { 'name': 'Sports Illustrated', 'price': 2, 'description': 'Adults playing with sticks' }
        }
      )
    except:
      self.fail('`_validate_shape_of_products` raised an exception')

  def test_validate_shape_of_products_is_invalid_due_to_parent_mistype(self):
    with self.assertRaisesRegex(TypeError, '`products` must be a dictionary'):
      self.subject(products = [])

  def test_validate_shape_of_products_is_invalid_due_to_children_products_value_mistype(self):
    with self.assertRaisesRegex(TypeError, 'Element in `products` must be a dictionary'):
      self.subject(products = { 'book': [] })

  def test_validate_shape_of_products_is_invalid_due_to_children_product_missing_required_keys(self):
    with self.assertRaisesRegex(KeyError, 'Product is missing the following keys: description'):
      self.subject(
        products = {
          'book': { 'name': 'Harry Potter', 'price': 1.00 }
        }
      )

    with self.assertRaisesRegex(KeyError, 'Product is missing the following keys: price'):
      self.subject(
        products = {
          'book': { 'name': 'Harry Potter', 'description': 'Kids playing with sticks' }
        }
      )

    with self.assertRaisesRegex(KeyError, 'Product is missing the following keys: name'):
      self.subject(
        products = {
          'book': { 'price': 1.00, 'description': 'Kids playing with sticks' }
        }
      )

    with self.assertRaisesRegex(KeyError, 'Product is missing the following keys: description, name, price'):
      self.subject(
        products = {
          'book': { }
        }
      )

  def test_validate_shape_of_products_is_invalid_due_to_children_products_values_mistype(self):
    with self.assertRaisesRegex(TypeError, 'Product key `name` must be of type'):
      self.subject(products = { 'book': { 'name': 1, 'price': 1.00, 'description': 'Kids playing with sticks' } })

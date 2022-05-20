from numbers import Real as real_number

class ProductsMixin:
    PRODUCT_KEYS_AND_TYPE = {
        'description': str,
        'name': str,
        'price': real_number
    }

    def _validate_shape_of_products(self, products):
        if not isinstance(products, dict):
            raise TypeError('`products` must be a dictionary')

        for product in products.values():
            self._validate_shape_of_product(product)

    def _validate_shape_of_product(self, product):
        if not isinstance(product, dict):
            raise TypeError('Element in `products` must be a dictionary')

        if not set(self.PRODUCT_KEYS_AND_TYPE.keys()).issubset(set(product.keys())):
            raise KeyError(f'Product is missing the following keys: {self._missing_keys(self.PRODUCT_KEYS_AND_TYPE.keys(), product.keys())}')

        for key, value in product.items():
            if not isinstance(value, self.PRODUCT_KEYS_AND_TYPE[key]):
                raise TypeError(f'Product key `{key}` must be of type `{str(self.PRODUCT_KEYS_AND_TYPE[key])}`')

    @staticmethod
    def _missing_keys(expected_keys, actual_keys):
        return ", ".join(sorted(list(expected_keys - actual_keys)))

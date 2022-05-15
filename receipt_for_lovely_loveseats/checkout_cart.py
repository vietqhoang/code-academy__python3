'''Module which is responsible for checkout cart'''

class CheckoutCart:
    '''Class that manages product checkout cart'''

    def __init__(self, products = None, items = None):
        self.products = products or {}
        self.items = items or []

    def add_to_checkout(self, product_key, count):
        '''Add a product and its quantity in checkout'''

        item = self._find_item(product_key)

        if item is None:
            self.items.append(self._item(product_key = product_key, count = count))
        else:
            self._increment_existing_item(item, count)

        return self.items

    def remove_from_checkout(self, product_key, count):
        '''Remove a product and its quantity in checkout'''

        item = self._find_item(product_key)

        if item is not None:
            self._decrement_existing_item(item, count)

        return self.items

    def _decrement_existing_item(self, item, reduction_count):
        if item['count'] - reduction_count <= 0:
            self.items.remove(item)

            return

        item['count'] -= reduction_count

    def _find_item(self, product_key):
        return next((item for item in self.items if item['product_key'] == product_key), None)

    @staticmethod
    def _increment_existing_item(item, additional_count):
        item['count'] += additional_count

    @staticmethod
    def _item(product_key, count):
        return { 'product_key': product_key, 'count': count }

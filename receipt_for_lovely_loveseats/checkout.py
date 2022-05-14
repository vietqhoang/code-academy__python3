'''Module which provides checkout related tools'''

class Checkout:
    '''Class that manages product checkout'''

    def __init__(self, products = None, items = None):
        self.products = products or {}
        self.items = items or []

    def add_to_checkout(self, product_key, count):
        '''Add a product and its quantity in checkout'''
        item = self.__find_item(product_key)

        if item is None:
            self.items.append(self.__item(product_key = product_key, count = count))
        else:
            self.__increment_existing_item(item, count)

        return self.items

    def remove_from_checkout(self, product_key, count):
        '''Remove a product and its quantity in checkout'''
        item = self.__find_item(product_key)

        if item is not None:
            self.__decrement_existing_item(item, count)

        return self.items

    def __decrement_existing_item(self, item, reduction_count):
        if item['count'] - reduction_count <= 0:
            self.items.remove(item)

            return

        item['count'] -= reduction_count

    def __find_item(self, product_key):
        return next((item for item in self.items if item['product_key'] == product_key), None)

    @staticmethod
    def __increment_existing_item(item, additional_count):
        item['count'] += additional_count

    @staticmethod
    def __item(product_key, count):
        return { 'product_key': product_key, 'count': count }

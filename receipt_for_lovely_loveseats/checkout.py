class Checkout:
  def __init__(self, products = {}, items = []):
    self.products = products
    self.items = items

  def add_to_checkout(self, product_key, count):
    item = self.__find_item(product_key)

    if item is None:
      self.items.append({ 'product_key': product_key, 'count': count })
    else:
      self.__increment_existing_item(item, count)

    return self.items

  def remove_from_checkout(self, product_key, count):
    item = self.__find_item(product_key)

    if item is not None:
      self.__decrement_existing_item(item, count)

    return self.items

  def __decrement_existing_item(self, item, count):
    if item['count'] - count <= 0:
      self.items.remove(item)

      return

    item_index = self.items.index(item)
    item['count'] -= count
    self.items[item_index] = item

  def __find_item(self, product_key):
    return next((item for item in self.items if item['product_key'] == product_key), None)

  def __increment_existing_item(self, item, count):
    previous_count = item['count']

    self.remove_from_checkout(product_key = item['product_key'], count = item['count'])
    self.items.append({ 'product_key': item['product_key'], 'count': previous_count + count })

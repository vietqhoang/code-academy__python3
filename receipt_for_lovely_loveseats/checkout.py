class Checkout:
  def __init__(self, products = {}, items = []):
    self.products = products
    self.items = items

  def add_to_checkout(self, product_key, count):
    item = self.__find_item(product_key)

    if item is None:
      self.items.append(self.__item(product_key = product_key, count = count))
    else:
      self.__increment_existing_item(item, count)

    return self.items

  def remove_from_checkout(self, product_key, count):
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

  def __increment_existing_item(self, item, additional_count):
    item['count'] += additional_count

  def __item(self, product_key, count):
    return { 'product_key': product_key, 'count': count }

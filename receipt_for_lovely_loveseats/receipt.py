class Receipt:
  def __init__(self, products = []):
    self.products = products

  def receipt_body(self, items = [], totals = {}):
    receipt_line_items = []

    receipt_line_items.append('Customer Items:')
    receipt_line_items.extend(self.__receipt_product_line_item_list(items))
    receipt_line_items.append('')
    receipt_line_items.append(f'Subtotal: ${self.__format_number(totals["subtotal"])}')
    receipt_line_items.append(f'Sales tax ({self.__format_number(totals["sales_tax_rate"] * 100)}%): ${self.__format_number(totals["sales_tax_total"])}')
    receipt_line_items.append(f'Total: ${self.__format_number(totals["total"])}')

    return '\n'.join(receipt_line_items)

  def __receipt_product_line_item(self, item_count, product):
    return f'* {item_count}x {product["name"]}: {product["description"]}'

  def __receipt_product_line_item_list(self, items):
    return list(map(lambda item: self.__receipt_product_line_item(item_count = item['count'], product = self.products[item['product_key']]), items))

  def __format_number(self, amount):
    return f'{amount:0.2f}'

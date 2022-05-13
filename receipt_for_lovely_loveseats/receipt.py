class Receipt:
  def __init__(self, products = []):
    self.products = products

  def receipt_body(self, items = [], totals = {}):
    receipt_line_items = []
    formatted_totals = self.__format_totals(totals)

    receipt_line_items.append('Customer Items:')
    receipt_line_items.extend(self.__receipt_product_line_item_list(items))
    receipt_line_items.append('')
    receipt_line_items.append(f'Subtotal: ${formatted_totals["subtotal"]}')
    receipt_line_items.append(f'Sales tax ({formatted_totals["sales_tax_rate"]}%): ${formatted_totals["sales_tax_total"]}')
    receipt_line_items.append(f'Total: ${formatted_totals["total"]}')

    return '\n'.join(receipt_line_items)

  def __receipt_product_line_item(self, item_count, product):
    return f'* {item_count}x {product["name"]}: {product["description"]}'

  def __receipt_product_line_item_list(self, items):
    return list(map(lambda item: self.__receipt_product_line_item(item_count = item['count'], product = self.products[item['product_key']]), items))

  def __format_number(self, amount):
    return f'{amount:0.2f}'

  def __format_totals(self, totals):
    new_totals = totals.copy()
    new_totals['sales_tax_rate'] *= 100

    return dict((key, self.__format_number(value)) for key, value in new_totals.items())

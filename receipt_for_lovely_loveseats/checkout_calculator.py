class CheckoutCalculator:
  def __init__(self, products = {}):
    self.items = []
    self.products = products

  def calculate_totals(self, items = [], sales_tax_rate = 0):
    self.items = items

    return {
      'subtotal': self.__calculate_subtotal(),
      'sales_tax_rate': sales_tax_rate,
      'sales_tax_total': self.__calculate_sales_tax_total(sales_tax_rate = sales_tax_rate),
      'total': self.__calculate_total(sales_tax_rate = sales_tax_rate)
    }

  def __calculate_sales_tax_total(self, sales_tax_rate):
    return self.__calculate_subtotal() * sales_tax_rate

  def __calculate_subtotal(self):
    return sum(map(lambda item: item['count'] * self.products[item['product_key']]['price'], self.items))

  def __calculate_total(self, sales_tax_rate):
    return self.__calculate_subtotal() + self.__calculate_sales_tax_total(sales_tax_rate)

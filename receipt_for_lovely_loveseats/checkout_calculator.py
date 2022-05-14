'''Module which is responsible for calculating an itemizations cost based on product information'''

class CheckoutCalculator:
    '''Class that calculates the cost totals for a list of items'''

    def __init__(self, products = None):
        self.items = []
        self.products = products or {}

    def calculate_totals(self, items = None, sales_tax_rate = 0):
        '''Calculate the subtotal, sales tax total, and total based on the items'''

        self.items = items or []

        return {
            'subtotal': self._calculate_subtotal(),
            'sales_tax_rate': sales_tax_rate,
            'sales_tax_total': self._calculate_sales_tax_total(sales_tax_rate = sales_tax_rate),
            'total': self._calculate_total(sales_tax_rate = sales_tax_rate)
        }

    def _calculate_sales_tax_total(self, sales_tax_rate):
        return self._calculate_subtotal() * sales_tax_rate

    def _calculate_subtotal(self):
        return sum(
            map(
                lambda item: item['count'] * self.products[item['product_key']]['price'],
                self.items
            )
        )

    def _calculate_total(self, sales_tax_rate):
        return (
            self._calculate_subtotal() +
            self._calculate_sales_tax_total(sales_tax_rate = sales_tax_rate)
        )

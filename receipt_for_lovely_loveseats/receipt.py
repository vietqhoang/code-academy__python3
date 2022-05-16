'Module which is responsible for receipts'

class Receipt:
    'Class that manages the generation of a receipt'

    def __init__(self, products = None):
        self.products = products or []

    def receipt_body(self, items = None, totals = None):
        'Returns the receipt string body'

        items = items or []
        totals = totals or {}

        receipt_line_items = []
        formatted_totals = self._format_totals(totals)

        receipt_line_items.append('Customer Items:')
        receipt_line_items.extend(self._receipt_product_line_item_list(items))
        receipt_line_items.append('')
        receipt_line_items.append(f'Subtotal: ${formatted_totals["subtotal"]}')
        receipt_line_items.append(
            f'Sales tax ({formatted_totals["sales_tax_rate"]}%): '
            f'${formatted_totals["sales_tax_total"]}'
        )
        receipt_line_items.append(f'Total: ${formatted_totals["total"]}')

        return '\n'.join(receipt_line_items)

    @staticmethod
    def _receipt_product_line_item(item_count, product):
        return f'* {item_count}x {product["name"]}: {product["description"]}'

    def _receipt_product_line_item_list(self, items):
        return [
            self._receipt_product_line_item(
                item_count = item['count'],
                product = self.products[item['product_key']]
            )
            for item in items
        ]

    @staticmethod
    def _format_number(amount):
        return f'{amount:0.2f}'

    def _format_totals(self, totals):
        new_totals = totals.copy()
        new_totals['sales_tax_rate'] *= 100

        return dict((key, self._format_number(value)) for key, value in new_totals.items())

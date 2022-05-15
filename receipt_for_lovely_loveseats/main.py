(
    'Integration example of checking out products, calculating the totals, '
    'and generating the receipt body'
)

from checkout_cart import CheckoutCart
from checkout_cart_calculator import CheckoutCartCalculator
from receipt import Receipt

PRODUCTS = {
    'lovely_loveseat': {
        'name': 'Lovely Loveseat',
        'description': (
        'Tufted polyester blend on wood. '
        '32 inches high x 40 inches wide x 30 inches deep. '
        'Red or white.'
        ),
        'price': 254.00
    },
    'stylish_settee': {
        'name': 'Stylish Settee',
        'description': (
        'Faux leather on birch. '
        '29.50 inches high x 54.75 inches wide x 28 inches deep. '
        'Black.'
        ),
        'price': 180.50
    },
    'luxurious_lamp': {
        'name': 'Luxurious Lamp',
        'description': 'Glass and iron. 36 inches tall. Brown with cream shade.',
        'price': 52.15
    }
}
SALES_TAX_RATE = 0.088

checkout_cart = CheckoutCart(products = PRODUCTS)

checkout_cart.add_to_checkout(product_key = 'stylish_settee', count = 4)
checkout_cart.add_to_checkout(product_key = 'luxurious_lamp', count = 2)
checkout_cart.add_to_checkout(product_key = 'lovely_loveseat', count = 5)
checkout_cart.remove_from_checkout(product_key = 'stylish_settee', count = 3)
checkout_cart.remove_from_checkout(product_key = 'luxurious_lamp', count = 2)

checkout_cart_calculator = CheckoutCartCalculator(products = PRODUCTS)
checkout_totals = checkout_cart_calculator.calculate_totals(
    items = checkout_cart.items,
    sales_tax_rate = SALES_TAX_RATE
)
receipt = Receipt(products = PRODUCTS)

print(receipt.receipt_body(items = checkout_cart.items, totals = checkout_totals))

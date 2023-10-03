product_list = [
    'Short Dress$24.99', 'Patterned Slacks$29.99', 'Short Chiffon Dress$49.99',
    'Off-the-shoulder Dress$59.99', 'V-neck Top$24.99', 'Short Chiffon Dress$49.99',
    'V-neck Top$24.99', 'V-neck Top$24.99', 'Short Lace Dress$59.99', 'Fitted Dress$34.99'
]

split_products = [item.split('$') for item in product_list]

# Тепер у вас є список, де кожний елемент - це список з назвою та ціною
for product in split_products:
    print("Назва:", product[0], ", Ціна:", product[1])

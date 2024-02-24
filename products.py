import itertools

rows_default, cols_default = 3, 2


def generate(rows):
    global rows_default

    if rows > 0:
        rows_default = rows

    products = [[None for _ in range(cols_default)] for _ in range(rows_default)]

    for row in range(rows_default):
        products[row][0] = f'Item {row + 1}'
        products[row][1] = (row + 1) * 200.0

    return products


def make_packs(products):
    global rows_default

    if len(products) > 0:
        packs = []

        for packs_size in range(2, len(products) + 1):
            for index, combinations in enumerate(itertools.combinations(products, packs_size)):
                combo_name = f'Combo {index + 1}(' + ' + '.join(
                    product[0].split()[1] if i > 0 else product[0] for i, product in enumerate(combinations)) + ')'
                combo_price = sum(product[1] for product in combinations)
                discount_rate = 25 if len(combinations) == len(products) > 0 else 10
                packs.append((combo_name, discount(discount_rate, combo_price)))

        return packs


def discount(percent, value):
    return value - (value / percent)

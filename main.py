import random
import products

if __name__ == "__main__":
    product_list = products.generate(3)
    combo_list = products.make_packs(product_list)

    print()
    print('Online Store')
    print('-' * 30)
    print(f'Product(s)\t\t\t\tPrice')

    for product in product_list:
        print('\t\t\t\t\t'.join(map(str, product)))

    for combo in combo_list:
        print('\t\t'.join(map(str, combo)))

    print()
    print('-' * 30)
    print(f'For delivery Contact: {random.randrange(10000000, 99999999)}')

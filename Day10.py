# SALES INVENTORY
items = {'bread': {'qty': 10, 'price':8, 'vendor':'crispy bakery', 'discount':'10%'},
         'milo': {'qty': 40, 'price':7, 'vendor':'jelly vendors', 'discount':'10%'}}

cart = {}

# qty_prompt = int(input())
# print("\nNested dictionary 2-")
# print(items)
# tobuy_item = input()
# their_item = tobuy_item.lower()

def re_launch():
    global qty_prompt
    qty_prompt = int(input())
    if qty_prompt <= (items[their_item]['qty']):
        total_price = qty_prompt*(items[their_item]['price'])
        # print("Total qty selected =",qty_prompt,
        #       "Total price =", total_price,"USD")

        # print("{:<15} {:<15} {:<15} {:<15}".format('ITEM', 'QTY', 'PRICE/UNIT($)', 'TOTAL PRICE($)'))
        # print("{:<15} {:<15} {:<15} {:<15}".format(their_item, qty_prompt, (items[their_item]['price']), total_price))
        # print("_________________________________________________________________________")
        # print("Thanks for your patronage")
        add_to_cart()
    elif qty_prompt >= (items[their_item]['qty']):
        print("Out of stock")
        launch()

furthermore = {"ITEMS": items, "QUANTITY": qty_prompt, "TOTAL PRICE": total_price}


def add_to_cart():
    if cart:
        cart[their_item] = qty_prompt, total_price
        print(cart, "cart has successfully been filled")
    else:
        cart.update(furthermore)
        print(cart, "cart added and updated")
    # else:
    #     print("Items isn't sold here")
    #     print("would you like to purchase something else? (Y/N)")
    #     restart_prompt1 = input()
    #     if restart_prompt1 == 'Y':
    #         launch()
    #     elif restart_prompt1 == 'N':
    #         print("Thanks for your patronage")


def launch():
    global tobuy_item, their_item
    print("WELCOME TO ROMMY'S MALL")
    print("what product is to be bought?")
    tobuy_item = input()
    their_item = tobuy_item.lower()
    if their_item in items.keys():
        print((items[their_item]['price']), "USD")
        print("How many is to be purcahased?")
    else:
        print("Item isn't sold here")
        print("would you like to purchase something else? (Y/N)")
        restart_prompt1 = input()
        if restart_prompt1 == 'Y':
            launch()
        elif restart_prompt1 == 'N':
            print("Thanks for your patronage")
    re_launch()


launch()
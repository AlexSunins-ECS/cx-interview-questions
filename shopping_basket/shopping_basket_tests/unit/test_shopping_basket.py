def test_shopping_basked_init_ok():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket(None, None)

    assert sh_b.item_quantity == 0


def test_shopping_basket_adds_item():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket(None, None)

    sh_b.add_item(name='banana', quantity=1)
    assert sh_b.item_quantity == 1

    sh_b.add_item(name='orange', quantity = 4)
    assert sh_b.item_quantity == 2

    sh_b.add_item(name='orange', quantity = 10)
    assert sh_b.item_quantity == 2


def test_shopping_basket_removes_item():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket(None, None)

    sh_b.add_item(name='banana', quantity=1)
    assert sh_b.item_quantity == 1

    sh_b.add_item(name='orange', quantity = 1)
    assert sh_b.item_quantity == 2

    sh_b.remove_item(name='orange', quantity=1)
    assert sh_b.item_quantity == 1

    assert sh_b.items[0]['name'] == 'banana'


def test_shopping_basket_item_quantity_updates_correctly():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket(None, None)

    sh_b.add_item(name='banana', quantity=1)

    sh_b.add_item(name='orange', quantity = 5)
    sh_b.add_item(name='orange', quantity = 10)

    basket_item = sh_b.search_item(name='orange')
    assert basket_item['quantity'] == 15


def test_shopping_basket_total_values_update_after_pricier_call():
    from shopping_basket.shopping_basket import ShoppingBasket
    from shopping_basket.shopping_catalogue import ShoppingCatalogue
    from shopping_basket.shopping_basket_pricier import ShoppingPricier
    from shopping_basket.shopping_basket_offers import ShoppingOffer_BuyXGetY
    from shopping_basket.shopping_basket_offers import ShoppingOfferCatalogue

    # create catalogue
    sh_catalogue = ShoppingCatalogue()
    sh_catalogue.add_item(name='baked_beans', price=0.99)
    sh_catalogue.add_item(name='biscuits', price=1.2)

    # create an offer catalogue and populate
    sh_offers = ShoppingOfferCatalogue()
    sh_offers.add_offer(ShoppingOffer_BuyXGetY(name='baked_beans', base_condition=2, added_value=1))

    # create basket
    sh_basket = ShoppingBasket(sh_catalogue, sh_offers)

    # add items to the basket
    sh_basket.add_item(name='baked_beans', quantity=4)
    sh_basket.add_item(name='biscuits', quantity=1)

    # trigger basket pricier
    sh_basket.calculate()

    assert sh_basket.total != 0
    assert sh_basket.total == 4.17
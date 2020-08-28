def test_shopping_basket_pricier():
    from shopping_basket.shopping_basket_pricier import ShoppingPricier

    sh_pricier = ShoppingPricier()

    assert sh_pricier.total == 0


def test_shopping_pricier_calculates_total_without_offers():
    from shopping_basket.shopping_basket import ShoppingBasket
    from shopping_basket.shopping_catalogue import ShoppingCatalogue
    from shopping_basket.shopping_basket_pricier import ShoppingPricier

    # create catalogue
    sh_catalogue = ShoppingCatalogue()
    sh_catalogue.add_item(name= 'apple', price=1)
    sh_catalogue.add_item(name='orange', price=2)
    sh_catalogue.add_item(name='banana', price=3)

    # create basket
    sh_basket = ShoppingBasket()

    # add first item to the basket
    sh_basket.add_item(name='banana', quantity=5)

    # create pricier and calculate basket value
    sh_pricier = ShoppingPricier()
    r = sh_pricier.calculate(sh_basket, sh_catalogue, None)
    assert r['sub_total'] == 15

    # add second item
    sh_basket.add_item(name='orange', quantity=10)
    r = sh_pricier.calculate(sh_basket, sh_catalogue, None)
    assert r['sub_total'] == 35

    # remove some of first item
    sh_basket.remove_item(name='banana', quantity=2)
    r = sh_pricier.calculate(sh_basket, sh_catalogue, None)
    assert r['sub_total'] == 29


def test_shopping_pricier_calculates_total_with_buy_x_get_y_offer():
    from shopping_basket.shopping_basket import ShoppingBasket
    from shopping_basket.shopping_catalogue import ShoppingCatalogue
    from shopping_basket.shopping_basket_pricier import ShoppingPricier
    from shopping_basket.shopping_basket_offers import ShoppingOffer_BuyXGetY
    from shopping_basket.shopping_basket_offers import ShoppingOfferCatalogue

    # create catalogue
    sh_catalogue = ShoppingCatalogue()
    sh_catalogue.add_item(name='banana', price=3)

    # create basket
    sh_basket = ShoppingBasket()

    # add first item to the basket
    sh_basket.add_item(name='banana', quantity=5)

    # create an offer catalogue and populate
    sh_offers = ShoppingOfferCatalogue()

    sh_offers.add_offer(ShoppingOffer_BuyXGetY(name='banana', base_condition=2, added_value=1))

    # create pricier and calculate basket value
    sh_pricier = ShoppingPricier()
    r = sh_pricier.calculate(sh_basket, sh_catalogue, sh_offers)

    assert r['sub_total'] == 15
    assert r['total'] == 12
    assert r['discount'] == 3


def test_pricier_result_using_sample_basket_one():
    from shopping_basket.shopping_basket import ShoppingBasket
    from shopping_basket.shopping_catalogue import ShoppingCatalogue
    from shopping_basket.shopping_basket_pricier import ShoppingPricier
    from shopping_basket.shopping_basket_offers import ShoppingOffer_BuyXGetY
    from shopping_basket.shopping_basket_offers import ShoppingOfferCatalogue

    # create catalogue
    sh_catalogue = ShoppingCatalogue()
    sh_catalogue.add_item(name='baked_beans', price=0.99)
    sh_catalogue.add_item(name='biscuits', price=1.2)

    # create basket
    sh_basket = ShoppingBasket()

    # add first item to the basket
    sh_basket.add_item(name='baked_beans', quantity=4)
    sh_basket.add_item(name='biscuits', quantity=1)

    # create an offer catalogue and populate
    sh_offers = ShoppingOfferCatalogue()
    sh_offers.add_offer(ShoppingOffer_BuyXGetY(name='baked_beans', base_condition=2, added_value=1))

    # create pricier and calculate basket value
    sh_pricier = ShoppingPricier()
    r = sh_pricier.calculate(sh_basket, sh_catalogue, sh_offers)

    assert "{:.2f}".format(r['sub_total']) == '5.16'
    assert "{:.2f}".format(r['total']) == '4.17'
    assert "{:.2f}".format(r['discount']) == '0.99'
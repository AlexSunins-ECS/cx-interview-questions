def test_shopping_basket_pricier():
    from shopping_basket.shopping_basket_pricier import ShoppingPricier

    sh_pricier = ShoppingPricier()

    assert sh_pricier.total == 0


def test_shopping_pricier_calculates_total():
    from shopping_basket.shopping_basket import ShoppingBasket
    from shopping_basket.shopping_catalogue import ShoppingCatalogue
    from shopping_basket.shopping_basket_pricier import ShoppingPricier

    # create catalogue
    sh_c = ShoppingCatalogue()
    sh_c.add_item(name= 'apple', price=1)
    sh_c.add_item(name='orange', price=2)
    sh_c.add_item(name='banana', price=3)

    # create basket
    sh_b = ShoppingBasket()

    # add first item to the basket
    sh_b.add_item(name='banana', quantity=5)

    # create pricier and calculate basket value
    sh_pricier = ShoppingPricier()
    r = sh_pricier.calculate(sh_b, sh_c)
    assert r['sub_total'] == 15

    # add second item
    sh_b.add_item(name='orange', quantity=10)
    r = sh_pricier.calculate(sh_b, sh_c)
    assert r['sub_total'] == 35

    # remove some of first item
    sh_b.remove_item(name='banana', quantity=2)
    r = sh_pricier.calculate(sh_b, sh_c)
    assert r['sub_total'] == 29
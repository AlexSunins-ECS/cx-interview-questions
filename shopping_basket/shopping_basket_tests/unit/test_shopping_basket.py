def test_shopping_basked_init_ok():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket()

    assert sh_b.item_quantity == 0


def test_shopping_basket_adds_item():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket()

    sh_b.add_item(name='banana', quantity=1)
    assert sh_b.item_quantity == 1

    sh_b.add_item(name='orange', quantity = 4)
    assert sh_b.item_quantity == 2

    sh_b.add_item(name='orange', quantity = 10)
    assert sh_b.item_quantity == 2


def test_shopping_basket_removes_item():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket()

    sh_b.add_item(name='banana', quantity=1)
    assert sh_b.item_quantity == 1

    sh_b.add_item(name='orange', quantity = 1)
    assert sh_b.item_quantity == 2

    sh_b.remove_item(name='orange', quantity=1)
    assert sh_b.item_quantity == 1

    assert sh_b.items[0]['name'] == 'banana'


def test_shopping_basket_item_quantity_updates_correctly():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket()

    sh_b.add_item(name='banana', quantity=1)

    sh_b.add_item(name='orange', quantity = 5)
    sh_b.add_item(name='orange', quantity = 10)

    basket_item = sh_b.search_item(name='orange')
    assert basket_item['quantity'] == 15
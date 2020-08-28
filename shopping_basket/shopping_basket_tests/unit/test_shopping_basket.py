def test_shopping_basked_init_ok():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket()

    assert sh_b.item_quantity == 0

def test_shopping_basket_adds_item():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket()

    sh_b.add('banana')
    assert sh_b.item_quantity == 1

    sh_b.add('orange')
    assert sh_b.item_quantity == 2

    sh_b.add('orange')
    assert sh_b.item_quantity == 2


def test_shopping_basked_removes_item():
    from shopping_basket.shopping_basket import ShoppingBasket

    sh_b = ShoppingBasket()

    sh_b.add('banana')
    assert sh_b.item_quantity == 1

    sh_b.add('orange')
    assert sh_b.item_quantity == 2

    sh_b.remove('orange')
    assert sh_b.item_quantity == 1

    assert sh_b.items[0] == 'banana'
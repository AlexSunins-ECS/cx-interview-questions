def test_shopping_catalogue_init_ok():
    from shopping_basket.shopping_catalogue import ShoppingCatalogue

    sh_c = ShoppingCatalogue()

    assert isinstance(sh_c.items, list)


def test_shopping_catalogue_adds_valid_item_and_ignores_invalid():
    from shopping_basket.shopping_catalogue import ShoppingCatalogue

    sh_c = ShoppingCatalogue()

    sh_c.add_item(name='apple', price= 1)

    assert sh_c.item_quantity == 1


def test_shopping_catalogue_does_not_add_already_existing_item():
    from shopping_basket.shopping_catalogue import ShoppingCatalogue

    sh_c = ShoppingCatalogue()

    sh_c.add_item(name='apple', price= 1)
    assert sh_c.item_quantity == 1

    sh_c.add_item(name='apple', price= 1)
    assert sh_c.item_quantity == 1


def test_shopping_catalogue_removes_item():
    from shopping_basket.shopping_catalogue import ShoppingCatalogue

    sh_c = ShoppingCatalogue()

    sh_c.add_item(name='apple', price= 1)
    assert sh_c.item_quantity == 1

    sh_c.add_item(name='orange', price= 2)
    assert sh_c.item_quantity == 2

    sh_c.remove_item('apple')
    assert sh_c.item_quantity == 1
    assert sh_c.items[0]['name'] == 'orange'


def test_shopping_catalogue_search_returns_valid_result():
    from shopping_basket.shopping_catalogue import ShoppingCatalogue

    sh_c = ShoppingCatalogue()

    sh_c.add_item(name='apple', price= 1)
    assert sh_c.item_quantity == 1

    sh_c.add_item(name='orange', price= 2)
    assert sh_c.item_quantity == 2

    search_result = sh_c.search_item('orange')
    assert search_result['price'] == 2


def test_shopping_catalogue_search_returns_none():
    from shopping_basket.shopping_catalogue import ShoppingCatalogue

    sh_c = ShoppingCatalogue()

    sh_c.add_item(name='apple', price= 1)
    assert sh_c.item_quantity == 1

    sh_c.add_item(name='orange', price= 2)
    assert sh_c.item_quantity == 2

    search_result = sh_c.search_item('banana')
    assert search_result is None
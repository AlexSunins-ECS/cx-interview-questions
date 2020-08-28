def test_handler_returns_200():
    from shopping_basket.handler import handler

    r = handler()

    assert r == 200
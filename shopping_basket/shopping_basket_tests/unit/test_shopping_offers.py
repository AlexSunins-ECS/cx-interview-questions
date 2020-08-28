def test_shopping_offer_catalogue_init_ok():
    from shopping_basket.shopping_basket_offers import ShoppingOfferCatalogue

    sh_offers = ShoppingOfferCatalogue()

    assert isinstance(sh_offers.offers, list)


def test_shopping_offer_catalogue_adds_item():
    from shopping_basket.shopping_basket_offers import ShoppingOfferCatalogue, ShoppingOffer_BuyXGetY

    sh_offers = ShoppingOfferCatalogue()
    sh_offers.add_offer(ShoppingOffer_BuyXGetY('beans', base_condition=2, added_value=1))

    assert len(sh_offers.offers) == 1


def test_shopping_offer_catalogue_search_returns_an_offer():
    from shopping_basket.shopping_basket_offers import ShoppingOfferCatalogue, ShoppingOffer_BuyXGetY

    sh_offers = ShoppingOfferCatalogue()
    sh_offers.add_offer(ShoppingOffer_BuyXGetY('beans', base_condition=2, added_value=1))

    offer_to_check = sh_offers.search('beans')

    assert offer_to_check.offer_result == 3
class ShoppingPricier():
    def __init__(self):
        self.total = 0
        self.sub_total = 0


    def calculate(self, basket, catalogue, offers=None):
        if basket.item_quantity == 0:
            return {'sub_total': 0, 'total': 0}

        if not basket:
            return {'sub_total': 0, 'total': 0}

        if not catalogue:
            return {'sub_total': 0, 'total': 0}

        self.total = 0
        self.sub_total = 0

        for item in basket.items:
            item_to_search = catalogue.search_item(item['name'])
            if item_to_search:
                # calculate raw price
                self.sub_total += item_to_search['price'] * item['quantity']

                # apply offers
                if offers:
                    item_is_on_offer = offers.search(item['name'])
                    if item_is_on_offer:
                        # update quantity in basket
                        new_basket_quantity = []
                        current_quantity = item['quantity']
                        offered_quantity = item_is_on_offer.offer_result

                        while 1:
                            if current_quantity > offered_quantity:
                                new_basket_quantity.append(offered_quantity)
                                current_quantity -= offered_quantity
                            else:
                                new_basket_quantity.append(current_quantity)
                                break

                        for each_new_quantity in new_basket_quantity:
                            if each_new_quantity == item_is_on_offer.offer_result:
                                self.total += item_to_search['price'] * item_is_on_offer.base_condition
                            else:
                                self.total += each_new_quantity * item_to_search['price']
                    else:
                        self.total += item_to_search['price'] * item['quantity']

        return {'sub_total': self.sub_total, 'total': self.total, 'discount': self.sub_total - self.total}
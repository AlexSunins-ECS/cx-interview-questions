class ShoppingOffer_BuyXGetY():
    def __init__(self, name, base_condition, added_value):
        self.type = 1
        self.name = name
        self.base_condition = base_condition
        self.added_value = added_value
        self.offer_result = self.base_condition + self.added_value


class ShoppingOffer_Discount():
    def __init__(self, name, discount_value):
        self.type = 2
        self.name = name
        self.discount_value = discount_value


    def discounted_price(self, price):
        return price - (price * (self.discount_value/100))


class ShoppingOfferCatalogue():
    def __init__(self):
        self.offers = []


    def add_offer(self, offer):
        self.offers.append(offer)


    def search(self, name):
        available_names = [k.name for k in self.offers]

        if name in available_names:
            for k in self.offers:
                if name.upper() == k.name.upper():
                    return k

            return None
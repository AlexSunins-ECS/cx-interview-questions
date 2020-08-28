class ShoppingPricier():
    def __init__(self):
        self.total = 0
        self.sub_total = 0


    def calculate(self, basket, catalogue):
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
                self.sub_total += item_to_search['price'] * item['quantity']

        return {'sub_total': self.sub_total, 'total': self.total}
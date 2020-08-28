from shopping_basket.shopping_basket_pricier import ShoppingPricier

class ShoppingBasket():
    def __init__(self, catalogue, offers=None):
        self.items = []
        self.item_quantity = 0
        self.total = 0
        self.sub_total = 0
        self.discount = 0
        self.pricier = ShoppingPricier()
        self.catalogue = catalogue
        self.offers = offers        


    def __update_item_count(self):
        self.item_quantity = len(self.items)


    def add_item(self, name, quantity):
        items_in_basket = [item['name'] for item in self.items]

        if name in items_in_basket:
            item_to_alter = self.search_item(name)
            self.items.remove(item_to_alter)
            item_to_alter['quantity'] += quantity
            self.items.append(item_to_alter)
        else:
            item_to_add = {'name': name, 'quantity': quantity}
            self.items.append(item_to_add)

        self.__update_item_count()


    def search_item(self, name):
        for item in self.items:
            if item['name'].upper() == name.upper():
                return item

        return None


    def remove_item(self, name, quantity):
        items_in_basket = [item['name'] for item in self.items]

        if name in items_in_basket:
            item_to_alter = self.search_item(name)

            if quantity > item_to_alter['quantity']:
                self.items.remove(item_to_alter)
                self.__update_item_count()
            else:
                self.items.remove(item_to_alter)
                item_to_alter['quantity'] -= quantity
                if item_to_alter['quantity'] > 0:
                    self.items.append(item_to_alter)
                self.__update_item_count()


    def calculate(self):
        r = self.pricier.calculate(self.items, self.catalogue, self.offers)
        self.sub_total = r['sub_total']
        self.total = r['total']
        self.discount = r['discount']
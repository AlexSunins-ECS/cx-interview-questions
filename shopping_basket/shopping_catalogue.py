class ShoppingCatalogue():
    def __init__(self):
        self.items = []
        self.item_quantity = 0


    def __update_item_quantity(self):
        self.item_quantity = len(self.items)


    def add_item(self, name, price):
        item_to_add = {'name': name, 'price': price}
        if not item_to_add in self.items:
            self.items.append(item_to_add)
            self.__update_item_quantity()


    def remove_item(self, item_name):
        for item in self.items:
            if item_name == item['name']:
                self.items.remove(item)
                self.__update_item_quantity()


    def search_item(self, item_name):
        if self.item_quantity != 0:
            for x in self.items:
                if x['name'].upper() == item_name.upper():
                    return x

            return None
        else:
            return None
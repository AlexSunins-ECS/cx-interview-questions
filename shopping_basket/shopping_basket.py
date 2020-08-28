class ShoppingBasket():
    def __init__(self):
        self.items = []
        self.item_quantity = 0

    def __update_item_count(self):
        self.item_quantity = len(self.items)

    def add(self, item):
        if not item in self.items:
            self.items.append(item)
            self.__update_item_count()

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            self.__update_item_count()
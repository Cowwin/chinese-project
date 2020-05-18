init python:
    class inventoryitem:
        def __init__(self, img, itemID, use):
            self.img = img
            self.itemID = itemID
            self.use = use
        def use(self, itemID, use):
                inventory.remove(self)

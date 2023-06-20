



class Item():
    def __init__(self, Name:str, Description:str, Amount:int=1) -> None:
        self.Name:str = Name
        self.Description:str = Description
        self.Amount:int = Amount
    def Check(self, _Item) -> bool:
        return self.Name == _Item.Name and self.Description == _Item.Description

class Items():
    Return:Item = Item("Return", "Return")
    Null:Item = Item("Null", "Null")
    Spoon:Item = Item("Spoon", "Can hurt people")
    Beans:Item = Item("Beans", "Beans")
    HouseKey:Item = Item("House Key", "Unlocks house")
    FlashLight:Item = Item("Flash Light", "Illuminates an area")
    Dime:Item = Item("Dime", "A coin")
    GoldCoin:Item = Item("Gold Coin", "A stamped coin made of gold")
    BobbyPin:Item = Item("Bobby pin", "Can be used to pick locks")
    ToothBrush:Item = Item("Tooth Brush", "Used")
    QTip:Item = Item("Q-tip", "Just a a-tip")
    NightStandKey:Item = Item("Night Stand Key", "Opens a night stand")


class Inventory():
    inventory:list = []
    slots:int = 12
    @staticmethod
    def hasItem(item:Item) -> bool:
        for itm in Inventory.inventory:
            itm:Item
            if itm.Check(item):
                return True
        return False
#Inventory.inventory[0].check(Items.Spoon)
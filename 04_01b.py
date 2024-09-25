from collections import namedtuple, defaultdict
from pprint import pprint

def get_dict(list_to_categorize):
    res = defaultdict(lambda:set())
    for item in list_to_categorize:
        if item.identifier[:3] == "BEV":
            res["beverages"].add(item)
        elif item.identifier[:3] == "STA":
            res["starter"].add(item)
        elif item.identifier[:3] == "DES":
            res["dessert"].add(item)
        elif item.identifier[:3] == "SAL":
            res["salad"].add(item)  
    return(res)        
            
def main():
    #add code here
    Food = namedtuple("Food", ["identifier", "name"])
    

    nadias_list = [
        Food("STA001",  "Panko Stuffed Mushrooms"),
        Food("BEV003",	"Cafe Latte"),
        Food("STA002",	"Mini Cheeseburgers"),
        Food("STA003",	"French Onion Soup"),
        Food("STA004",	"Artichokes with Garlic Aioli"),
        Food("STA005",	"Parmesan Deviled Eggs"),
        Food("SAL001",	"Garden Buffet"),
        Food("SAL002",	"House Salad"),
        Food("SAL003",	"Chefs Salad"),
        Food("SAL004",	"Quinoa Salmon Salad"),
        Food("ENT001",	"Classic Burger"),
        Food("ENT002",	"Tomato Bruschetta Tortellini"),
        Food("ENT003",	"Handcrafted Pizza"),
        Food("ENT004",	"Barbecued Tofu Skewers"),
        Food("ENT005",	"Fiesta Family Platter"),
        Food("DES001",	"Creme Brulee"),
        Food("ENT001",	"Classic Burger"),
        Food("DES002",	"Cheesecake"),
        Food("DES003",	"Chocolate Chip Brownie"),
        Food("DES004",	"Apple Pie"),
        Food("STA001",	"Panko Stuffed Mushrooms"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV001",	"Tropical Blue Smoothie"),
        Food("BEV002",	"Pomegranate Iced Tea"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV003",	"Cafe Latte"),
        Food("DES005",	"Mixed Berry Tart"),
        Food("BEV003",	"Cafe Latte"),
    ]
    o = get_dict(nadias_list)
    pprint(o)
    return

if __name__ == "__main__":
    main()
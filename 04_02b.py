from collections import namedtuple
from collections import defaultdict
from collections import Counter
import pprint
import csv

#Calulating
#How many each product she has sold
#Data/OrderItems.csv
#DefaultDict



def main():
    file_path = "data/OrderItems.csv"
    food_list = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        tuple_header = namedtuple('Headerfield', next(csv_reader))
        for row in csv_reader:
            food_list.append(tuple_header(*row))
    pprint.pprint(food_list, indent=2)
    res = defaultdict(int)
    for item in food_list:
        res[item.ProductID] += int(item.Quantity)
    pprint.pprint(res, indent=0)
            

    return

if __name__ == "__main__":
    main()
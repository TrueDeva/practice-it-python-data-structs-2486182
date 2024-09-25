import csv
from collections import namedtuple

def main():
    # Define the file path
    file_path = 'data/Customer.csv'

    # Open the file using 'with open'
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        # Optionally, read the header if the CSV has one

        header_namedtuple = namedtuple('Headerfield', next(csv_reader))
        #print(f"Header: {header_namedtuple}")
        #row1 = next(csv_reader)
        #print(row1)
        #print(header_namedtuple.index)
        #print(type(row1))
        #print(type(csv_reader))


        
        # Read the rest of the lines and create workable objects
        for row in csv_reader:
            # Here, you could transform each row into a more complex object if needed
            # For simplicity, we'll just print each row
            #print(row)
            htp = header_namedtuple(*row)
            print(htp.FirstName)
            

if __name__ == "__main__":
    main()

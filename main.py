import csv

animal_type = input("Which adoptable animals do you want to see? ")
animal_type = animal_type.strip().lower()

try:
    if 'cat' in animal_type:
        file_path = "data/cats.csv"

    if 'dog' in animal_type:
        file_path = "data/dogs.csv"

    data = []
    with open(file_path, 'r') as csvfile:
        doc = csv.reader(csvfile)
        for row in doc:
            data.append(row)
except:
    print("We only have cats and dogs here.")

# print data
for i in range(1, len(data), 1):
    print(f"{data[i][0]} is a {data[i][1]} year old {data[i][2]}.")





import os
import csv


def get_data():
    arr = os.listdir("./CSV/")
    data = []
    for el in arr:
        with open("./CSV/"+el, "r", encoding="windows-1250") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                data.append(row)
    return data


if(__name__ == '__main__'):
    print(get_data())

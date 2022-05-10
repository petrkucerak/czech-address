import os
import csv


def get_data():
    print("Start reading ...")
    counter = 0
    arr = os.listdir("./CSV/")
    data = []
    header = ""
    for el in arr:
        with open("./CSV/"+el, "r", encoding="windows-1250") as file:
            csvreader = csv.reader(file, delimiter=";")
            for row in csvreader:
                if header == "":
                    header = row
                if row != header:
                    data.append(row)
        counter += 1
        if(counter % 5000 == 0):
            print("...")
    print("Reading is done!")
    return data


def generate_file(data):
    print("Start with an exporting ...")
    counter = 0
    with open("./big-data.sql", "w+", encoding="utf-8") as file:
        file.write(
            'INSERT INTO "Adresa" ("ulice", "c.p.", "mesto", "PSC", "zeme")\n')
        file.write('VALUES')
        for row in data:
            file.write("('{ulice}', '{cp}', '{mesto}', '{PSC}', 'Česká Republika'),\n".format(
                ulice=row[10], cp=row[12], mesto=row[2], PSC=row[15]))

            counter += 1
            if(counter % 100000 == 0):
                print("...")
    print("File was exported!")


if(__name__ == '__main__'):
    data = get_data()
    generate_file(data)

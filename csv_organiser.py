#create a file that concatenates every other line in a csv file to fix faulty formatting from download

#import pandas as pd
import csv

#sort lines into date and price lists
def extract_columns(file_name):
    with open(file_name, 'r') as bad_file:
        reader = csv.reader(bad_file)
        x = 0
        date = []
        price = []
        for row in reader:
            row = "".join(row)
            if x == 0:
                date.append(row)
                x += 1
            elif x == 1:
                price.append(row)
                x -= 1
        return (date, price)

#rewrite csv file with date and corresponding price in the same row
def create_new_csv(date, price, file_name):
    name = (file_name.split("."))[0]
    with open(f"{name}_ammended.csv", "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["Date", "Price"])
        writer.writeheader()
        print("hello")
        for i in range(len(date)):
            writer.writerow({"Date": date[i], "Price": price[i]})
    print("hello")


def main():
    date, price = extract_columns("APPL_2023_data.csv")
    create_new_csv(date, price, "APPL_2023_data.csv")

main()

import csv

def read_file_into_array():
    with open('IRIS.csv', newline='') as csvfile:
         data = list(csv.reader(csvfile))
         print(data)


def read_csv_pd():

read_csv_pd()
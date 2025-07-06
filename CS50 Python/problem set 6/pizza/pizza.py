import csv
import sys
from tabulate import tabulate

def check_pizza_py():
    if len(sys.argv)<2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>2:
        sys.exit("Too much command-line arguments")
    else:
        if sys.argv[1].endswith(".csv")==False:
            sys.exit("Not a CSV file")

def get_Sicilian_csv(filename):
    with open (filename) as file:
        csv_list=[]
        for row in csv.reader(file):
            csv_list.append(row)
        data_list=tabulate(csv_list[1:],headers=csv_list[0] ,tablefmt="grid")
        print(data_list)

def get_Regular_csv(filename):
    with open (filename) as file:
        csv_list=[]
        for row in csv.reader(file):
            csv_list.append(row)
        data_list=tabulate(csv_list[1:],headers=csv_list[0] ,tablefmt="grid")
        print(data_list)

def main():
    check_pizza_py()
    if sys.argv[1]=='regular.csv':
        get_Regular_csv(sys.argv[1])
    else:
        get_Sicilian_csv(sys.argv[1])


if __name__ == "__main__":
    main()

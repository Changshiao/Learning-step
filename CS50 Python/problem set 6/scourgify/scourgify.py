import sys
import csv

def main():
    data=[]
    check_format()
    data=read_csvfile()
    write_csvfile(data)

#check
#read in
#output

def check_format():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    else:
        if '.csv'  not in sys.argv[1]:
            sys.exit("Could not read invalid_file.csv")


#接入文件到列表
def read_csvfile():
    data=[]
    try:
        with open(sys.argv[1], 'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                last_name,first_name=row["name"].replace(" ","").split(",")
                data.append({'first':first_name,'last':last_name,'house':row['house']})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")
    return data


#写入文件到after
def write_csvfile(data):
    try:
        with open(sys.argv[2], 'w') as file:
            writer=csv.DictWriter(file,fieldnames=["first","last","house"])
            writer.writerow({"first":"first","last":"last","house":"house"})
            for row in data:
                writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})
    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")

if __name__ == "__main__":
    main()

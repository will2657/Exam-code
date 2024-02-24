import csv

def myfunction(file_name):
    csv_open = open(str(file_name),"r")
    lust = []
    
    for line in csv_open:
        print(line)
        lust.append(line.split())
    print(lust)
    return lust
myfunction("-1.csv")               
    
import csv

def myfunction(nb):
    lust = []
    if nb > 0:
        print("the following values are between,", nb,"and 0")
        for x in range(nb+1):
           print(x)
           lust.append(x)
    elif nb == 0:
        print("The number = 0")
    else:
         print("the following integers are between", nb,"and 0")
    while nb <= 0:
        lust.append(nb) 
        print(nb)
        nb = nb + 1
        
            
    
    print(lust)
    with open(str(nb) + ".csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
                            
        writer.writerow(lust)
       

myfunction(9)
myfunction(0)
myfunction(-7)

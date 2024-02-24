TwoDimArray = (("blue", "green", "yellow"),(34, 23, 101))
counter = 0
for array in TwoDimArray :
    for item in array:
        counter += 1
        print("Elemnt number", str(counter),  "is",str(item))

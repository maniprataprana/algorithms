values = [2, 3, 2, 4]

def my_transformation(num):
    return num ** 2

for i in  map(my_transformation, values):
    print i
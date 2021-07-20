import datetime

def respprint(obj):
    if type(obj) == str:
        print(obj)
    else:
        keys = list(obj[0].keys())
        for item in keys:
            print("{0:20s}".format(item), end='')
        print()
        for item in obj:
            for element in item:
                print("{0:20s}".format(str(item[element])), end='') 
            print()
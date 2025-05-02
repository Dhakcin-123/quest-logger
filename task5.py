def describeitem(name,quantity):
    if quantity >= 2:
        print(f"{name}s:{quantity}")
    else:
        print(f"{name}:{quantity}")  
    return()

describeitem("banana",1)
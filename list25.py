list1=[1,50,24,69,15]
b=int(input("Nhap mot so:"))

if b not in list1:
    print("Not found in our list")
else:
    print("Found,position is", list1.index(b))
        
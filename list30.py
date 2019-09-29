number=list(map(int,input("Nhap day so").split()))
print(*number,sep=",")
print("Cac so chan trong day la")

for i in number:
    if(i%2)==0:
        print(i)
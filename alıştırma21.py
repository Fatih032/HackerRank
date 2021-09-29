if __name__ == '__main__':
    n = int(input("Dizi eleman sayısını giriniz:"))
    arr = map(int, input("Elemanları boşluk bırakarak giriniz:").split())
    
big, sbig = -6000, -6000
for i in arr:
    if (i > big):
        big, sbig = i, big
    elif (i < big and i > sbig):
        sbig = i
print (sbig)
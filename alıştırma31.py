n = int(input("Bir sayı giriniz:"))

count = 0
a=0
while n:
    
    print(n, end=" ")
    a = bin(n)
    n &= n << 1
    
    print(a)
    count += 1

print("sayı",count)


print("girilen sayının bölenlerini bulan python programı")


n = int(input("Bir sayı giriniz:"))
sum = 0
for i in range(1, n+1):
    if(n%i==0):
        sum = i+sum
    else:
        breakpoint         

print(sum)
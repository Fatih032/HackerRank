n = int(input())
for i in range(1, n+1):
    kelime1 = list(input())
    for i in range(0,len(kelime1)):
        if(i%2==0):
            print(kelime1[i], end="")
    print(" ", end="")
    for i in range(0, len(kelime1)):
        if(i%2==1):
            print(kelime1[i], end="") 
    print("")

    
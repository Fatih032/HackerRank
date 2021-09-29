from typing import List


List1=[1,4,7,0,5,3,7,5]
#List1.append(5)

#print(List1)

#List1.insert(0, 4)

#print(List1)

#List1.pop()

#print(List1)

#List1.remove(7)

#print(List1)

#List1.sort()

#print(List1)

#List1.sort()

#print(List1[0])
işlem = input("yapılacak işlemi yazınız:")
if(işlem=="insert"):
    List1.insert(int(input("indexi giriniz:")), int(input("değeri giriniz:")))
elif("pop"==işlem):
    List1.pop()
elif("append"==işlem):
    List1.append(int(input("değeri giriniz:")))

print(List1)
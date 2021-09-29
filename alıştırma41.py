a = int(input())
b = int(input())
lst=[]
lst.append(a//b)
lst.append(a%b)
lst=tuple(lst)
print(a//b)
print(a%b)
print(lst)
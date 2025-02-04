a=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("Enter the element:"))
    a.append(ele)
print(a)
a.sort()
print(a[-3])
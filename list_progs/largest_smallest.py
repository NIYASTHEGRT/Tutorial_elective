a=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    ele=int(input("Enter the element:"))
    a.append(ele)
print(a)
a.sort()
x=max(a) # type: ignore
y=min(a)
print("The max value is ",x)
print("The minimum value is ",y)

a=[]

n=int(input("Enter the number of elements in the list:"))

for i in range(0,n):
    ele=int(input("Enter the element:"))
    a.append(ele)

print(a)
#code
b=[]
for i in range(0,n):
    if(a[i]%2==0):
        b.append(a[i])
b.sort()
print("The new sorted list is ",b)